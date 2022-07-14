# Get the sample message
with open("./Input/Letters/starting_letter.txt") as file:
    template = file.read()

# Get a list of names
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

# Generate letters
for name in names:
    name = name.strip()
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as file:
        message = template.replace("[name]", name)
        file.write(message)
