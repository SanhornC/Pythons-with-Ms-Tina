'''

Study Drill 1 :
    flowchart graphically represents the flow of a program

    Types of Flowcharts
    1. Oval = start/end
    2. Parallelogram = input/output
    3. Rectangle = calculations
    4. Diamond = Selection Structures

'''
from sys import exit

# prints stuff, uses if-else statements
def gold_room():
    print("This room is full of gold. How much do you take?")
    
    next = input("> ") # next's value is given here
    if "0" in next or "1" in next: #5. possible to loop through it; yes 
        how_much = int(next) #don't have to be this complicated, use if statement? 
        #int() works like int ex: int('5') = 5, make string int
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!") 
        exit(0)
    else:
        dead("You greedy bastard!")
# Function, prints stuff, uses while loop and if-else statements 

def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print ("I got no idea what that means.")

# Function, prints stuff and contains if-else statements
def cthulhu_room():
    print ("Here you see the great evil Cthulhu.")
    print ("He, it, whatever stares at you and you go insane.")
    print ("Do you flee for your life or eat your head?")

    next = input("> ") # this is where next gets its another value, it will replace the original one

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# This is a function, prints stuff, contains if-else statements in between
def hidden_room():
    print("you look up and you see a hidden room. you see a button, press or stay")
    next=input("> ") # new value
    if "press" in next:
        print("explosion ur dead")
    else:
        print("you starve to death")

# This is another function, it prints stuff and exit(0)
def dead(why):
    print (why, "Good job!")
    exit(0)

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left. Or maybe you look up.")
    print ("Which one do you take?")

    next = input("> ") # new value, 

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    elif next == "up":
        hidden_room()
    else:
        dead("You stumble around the room until you starve.")

# variable next isn't a trouble though being used in several functions
# while loop does end
# if statement without else works fine
# I understand all of them

start()
