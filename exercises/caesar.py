import os
clear = lambda: os.system('clear')
clear()

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# Initialise alphabet list
alphabet = list("abcdefghijklmnopqrstuvwxyz")

def encrypt(message, num):
    encrypted_message = ""
    for c in message:
        # If its a letter in the alphabet, change it (leaving spaces and punctuation)
        if c in alphabet:
            # Get the new index based on shift amount input
            shift_index = alphabet.index(c) + num
            if shift_index > (len(alphabet) - 1):
                shift_index -= (len(alphabet) - 1)
            elif shift_index < 0:
                shift_index += (len(alphabet) - 1)
            
            # Get the encrypted character and add it to the message    
            encrypted_message += alphabet[shift_index]
        
        # Else leave it be   
        else:
            encrypted_message += c
            
    return encrypted_message

 
while True:
    print(logo)
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if choice == "encode":
        message = list(input("\nEnter your message: \n").lower())
        shift_num = int(input("\nEnter an encryption number: \n"))
        print("\nHere is your encrypted message:\n")
        print(encrypt(message, shift_num))
    elif choice == "decode":
        message = list(input("\nEnter message to decrypt: \n").lower())
        shift_num = int(input("\nEnter a decryption number: \n"))
        print("\nHere is your decrypted message:\n")
        print(encrypt(message, -shift_num))
    else:
        print("Sorry, command not recognised, please try again.")
        
    exit = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
    if exit == "no":
        break
    else:
        clear()
        





