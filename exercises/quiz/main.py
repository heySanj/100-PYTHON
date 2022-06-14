def clear():
    from os import system, name  
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

class User:
    def __init__(self, name, location):
        # Initialise attributes
        self.name = name
        self.location = location
        self.followers = 0
        self.following = 0
    
    def say_hi(self):
        print(f"Hi there! I'm {self.name} from {self.location}.")
        
    def follow(self, user):
        user.followers += 1
        self.following += 1        

user_1 = User("Sanj", "Brisbane")
user_2 = User("Sareeka", "Brisbane")

user_1.say_hi()
user_2.say_hi()

user_1.follow(user_2)
user_2.follow(user_1)

print(user_2.followers)


