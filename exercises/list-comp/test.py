def clear():
    from os import system, name

    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
clear()

# numbers = [1,2,3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = 'Angela'
# new_list = [letter for letter in name]
# print(new_list)

# doubled = [n * 2 for n in range(1,5)]
# print(doubled)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# upper = [name.upper() for name in names if len(name) >= 5]
# print(upper)

# import random
# scores = {name:random.randint(0,100) for name in names}
# passed = {name:score for (name, score) in scores.items() if score >= 60}
# print(scores)
# print(passed)

import pandas as pd

student_dict = {
    'student': ['Angela' , 'James', 'Lily', 'Sanjeev'],
    'score': [56, 76, 98, 99]
}

student_df = pd.DataFrame(student_dict)

# Looping through rows of a data frame (rather than columns)
# Each row will be returning a Series object
for (index, row) in student_df.iterrows():
    print(f"{row.student} scores {row.score}")