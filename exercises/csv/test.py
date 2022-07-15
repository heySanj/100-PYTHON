def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

def c_to_f(c):
    return ((c * 9/5) + 32)

# GETTING DATA USING OPEN METHOD  
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
    
    
# GETTING DATA USING CSV LIBRARY 
# import csv
# with open("weather_data.csv") as file:
#     data = list(csv.reader(file))
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))        
#     print(temperatures)


    
# GETTING DATA USING PANDAS
import pandas as pd
data = pd.read_csv("./data/weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# Get DATA in Row
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(c_to_f(int(monday.temp)))


# Create data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

grades = pd.DataFrame(data_dict)

grades.to_csv("./data/grades.csv")
