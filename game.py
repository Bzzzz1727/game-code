import random

# Opening files
try:
    bal = open("coins.txt", "r+")
    inv = open("inv.txt", "r+")
except FileNotFoundError:
    bal = open("coins.txt", "a+")
    inv = open("inv.txt", "a+")

# Here are all the variables
coins = bal.read().strip()  # Existing coins from the user
chitin = int(coins) if coins else 0  # Convert coins to an integer or default to 0
items = inv.read().strip()  # Existing items on the user
item = items.split(',') if items else []  # Split items by comma and store in a list

def add_coins(x):
    global chitin
    chitin += x
    with open("coins.txt", "r+") as bal:
        bal.seek(0)  # Move the cursor to the beginning of the file
        bal.truncate()  # Clear the file content
        bal.write(str(chitin))  # Write the updated value

def add_inv(x):
    global item
    item.append(x)
    with open("inv.txt", "r+") as inv:
        inv.seek(0)  # Move the cursor to the beginning of the file
        inv.truncate()  # Clear the file content
        inv.write(','.join(item))  # Write the updated items
# Command list
def commands():
    print("balance - check your balance")
    print("inventory - shows items in your inventory")
    print("commands - displays all commands")
    print("hunt - hunt animals")
    print("marry - to get married to the love of your life")
    print("divorce - divorce your partner")
    print("beg - beg for some changes from a stranger")
    print("work - work to make money")

# Welcome!
print("Welcome to Liganin Land")
command = input("Would you like to see commands? (y/n)")
if command.lower() == "y":
    commands()

# Functions
def balance():
    print("Your balance: ", chitin)

def inventory():
    print("Your inventory: ", item)

def hunt():
    animals = ["pig", "donkey", "deer", "bear", "wolf", "rabbit", "Zebra", "sheep", "hen", "cow", "goat"]
    x = random.choice(animals)
    add_inv(x)
    print("You hunted a", x)

def marry():
    if "ring" in item:
        print("You're already married, don't try to cheat!")
    else:
        add_inv("ring")
        print("Congratulations on getting married! Here's your ring.")

def divorce():
    if "ring" in item:
        item.remove("ring")
        print("I am taking my ring away.")
    else:
        print("Get married first, loner!")

def beg():
    n = random.randint(1, 50)
    print("Here you go, little beggar. ", n, "chitins for you.")
    add_coins(n)

def work():
    b = random.randint(100, 5000)
    print("Thank you for your hard work. ", b, "chitins credited to your account.")
    add_coins(b)

# User interface
while True:
    user_input = input("Enter the command: ")
    if user_input.lower() == "balance":
        balance()
    elif user_input.lower() == "inventory":
        inventory()
    elif user_input.lower() == "commands":
        commands()
    elif user_input.lower() == "hunt":
        hunt()
    elif user_input.lower() == "marry":
        marry()
    elif user_input.lower() == "divorce":
        divorce()
    elif user_input.lower() == "beg":
        beg()
    elif user_input.lower() == "work":
        work()
