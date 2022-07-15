def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

import pandas as pd
data = pd.read_csv("./data/squirrel_data.csv")
colours = data["Primary Fur Color"].value_counts()

colours = colours.to_dict()
# print(colours)

data_dict = {
    "Fur Colour": list(colours.keys()),
    "Count" : list(colours.values())    
}

squirrels = pd.DataFrame(data_dict)
squirrels.to_csv("./data/squirrel_colours.csv")