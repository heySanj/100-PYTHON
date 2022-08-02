def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()


from msilib.schema import Error
import os, zipfile
from tkinter import *
from tkinter import filedialog, messagebox

FONT = ("Arial", 12, "bold")
BG_COLOUR = "#fcfae9"
THEME_COLOUR = "#f8246b"
TEXT_COLOUR = "#474747"

GREEN = "#6d9b03"
RED = "#b92500"

global ZIPS
ZIPS = []
TARGET_EXT = ".zip"

# ---------------------------- FUNCTIONS ------------------------------- #

# Unzip all the files in a list of Zips
def unzip(zips: list):
    if len(zips) > 0:
        try:
            for file in zips:

                # Get the file path and create a ZipFile object
                file_path = os.path.abspath(file)        
                zip_ref = zipfile.ZipFile(file_path)            
                
                # Create a New Folder using the same name as the ZIP file, with the '.zip' removed
                new_directory = file_path[:-4]
                if not os.path.exists(new_directory):
                    os.mkdir(new_directory)        
                
                # Extract the contents to the newly created directory
                zip_ref.extractall(new_directory)
                zip_ref.close() # close file
                
        except Exception as error_message:
            # Output error Message
            output_text.config(text=f"Error: {error_message}", fg=RED)
        
        else:
            # Output success Message
            output_text.config(text=f"Successfully unzipped {len(zips)} files.", fg=GREEN)
    
    # No zips
    else:
        # Output message of found zip files
        output_text.config(text=f"No .zip files found.", fg=TEXT_COLOUR)
        

def delete_zips(zips: list):
    
    if len(zips) > 0:
        answer = messagebox.askyesno(title=f'Delete Files', message=f'Are you sure you want to permanently delete {len(zips)} .zip files?')        
        if answer:
            global ZIPS
            try:
                for file in zips:
                    os.remove(file) # Delete the file
                    
            except Exception as error_message:
                # Output error Message
                output_text.config(text=f"Error: {error_message}", fg=RED)
            
            else:
                # Output success Message
                output_text.config(text=f"Successfully deleted {len(zips)} files.", fg=GREEN)
                
                # Remove the files from ZIPS variable
                ZIPS = []


# Return a string that directs to a folder
def select_folder():
    
    global ZIPS
    
    # Allow the user to browse to folder
    target_dir = filedialog.askdirectory()
       
    # Change to target directory holding .zip files
    try:
        os.chdir(target_dir)
    except Exception as error_message:
        # Output error Message
        # output_text.config(text=f"Error: {error_message}")
        output_text.config(text="No folder selected.")
    else:
        # Put the directory in the text field after clearing it
        file_text.config(state='normal')
        file_text.delete(1.0,'end')
        file_text.insert('end', target_dir) 
        file_text.config(state='disabled')
        
        # Find the zip files
        ZIPS = find_zips(target_dir)
        
        # Output message of found zip files
        output_text.config(text=f"{len(ZIPS)} .zip files were found.", fg=TEXT_COLOUR)
    

    
# Get a list of zip files
def find_zips(directory: str):
        
    zip_files = []  
      
    # Loop through all files in target directory
    for file in os.listdir(directory):
        # If the file is of target type, add it to the list
        if file.endswith(TARGET_EXT): 
            zip_files.append(file)
            
    return zip_files
        
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Unzipper")
window["bg"] = BG_COLOUR
window.config(padx=20,pady=20)

# GRID ------------------------ 2 columns, 4 rows

# Logo
logo = Label(text="UnZipper", font=("Arial Black", 36, "bold"), bg=BG_COLOUR, fg=THEME_COLOUR)
logo.grid(column=0,row=0,columnspan=2,pady=5)

# Text Fields
file_text = Text(font=("Arial", 9, "italic"), bg=BG_COLOUR, fg=TEXT_COLOUR, width=80,height=3, state='disabled')
file_text.grid(column=0,row=1,pady=5)

# Output Text
output_text = Label(text="No folder selected.", font=("Arial", 18, "bold"), bg=BG_COLOUR, fg=TEXT_COLOUR, width=50, height=2, wraplength=600)
output_text.grid(column=0,row=2,columnspan=2,pady=5)

# Buttons
btn_select = Button(width=15,text="Select Folder",font=FONT,padx=10,pady=10, command=select_folder)
btn_unzip = Button(width=15,text="Unzip!",font=FONT,padx=10,pady=10, command= lambda: unzip(ZIPS))
btn_delete = Button(width=15,text="Delete Zips",font=FONT,padx=10,pady=10, command= lambda: delete_zips(ZIPS))

btn_select.grid(column=1,row=1,pady=5)
btn_unzip.grid(column=0,row=3,pady=5,padx=10, sticky="news")
btn_delete.grid(column=1,row=3,pady=5,padx=10)

window.mainloop()