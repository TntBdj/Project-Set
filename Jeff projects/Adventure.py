#since its a buch of functions calling functions the start is the end and the end is the start
#importing Pillow
from PIL import Image 
#restart if you want
def Walk():
    while True:
        Input = input("You see light at the end of a path. Do you want to go to it(g) or turn back(b): ")
        if Input.lower() == "g":
            print("the light is actually a car coming towards you. You end up running straing to your death. \nThe end.")
            quit()
        elif Input.lower() == "b":
            Start()
        else:
            print("Invalid response")
            continue     

#more clif decisions
def Climb():
    while True:
        Input = input("while climbing you see a short cut, but it's risky. \nWould you like to take the risk(r) or keep going the long way(l): ")
        if Input.lower() == "r":
            print("You take the risk and it pays off. You are now at the top of the clif")
            Walk()
        elif Input.lower() == "l":
            print("You realize this route was way too long and your arms get tired. your fingers slip and you fall to your death. \nThe end.")
            quit()
        else:
            print("Invalid response")
            continue     

#suicide?
def Leave():
    while True:
        cliff = Image.open('cliff.jpg')
        cliff.show()
        Input = input("You leave and keep following the path to the edge of a clif. would you like to jump(j) or go back(b): ")
        if Input.lower() == "j":
            print("Take the leap and fall all the way to the bottom. Your head smashed into the floor and explodes into a million pieces. \nThe end.")
            quit()
        elif Input.lower() == "b":
            Walk()
        else:
            print("Invalid response")
            continue       

#back to a clif
def NoParties():
    while True:
        bottom_cliff = Image.open('bottom_cliff.jpg')
        bottom_cliff.show()
        Input = input("you go outside the abandoned house and find yourself at the bottom of a cliff .\nWould you like to climb it(c) or keep walking(w)")
        if Input.lower() == "c":
            Climb()
        elif Input.lower() == "w":
            Walk()
        else:
            print("Invalid response")
            continue       

#Best possible ourcome is here
def Document():
    while True:
        Input = input("you successfully document the new creatures and post your findings. Do you like parties? (y/n): ")
        if Input.lower() == "y":
            money = Image.open('money.jpg')
            money.show()
            print("You get home, celebrate you findings and make millions. The end")
            quit()
        elif Input.lower() == "n":
            NoParties()
        else:
            print("Invalid response")
            continue   

#what happens inside the house
def Enter():
    while True:
        Input = input("Inside you find out the house is a filled with all sorts of creatures that have never been seen before \nWould you like to kill(k) or document them for research(d): ")
        if Input.lower() == "k":
            print("you end up successfully killing half of them untill you get to a small cat looking creature. You let your guard down and tentacles from inside the cats mouth reach out grab your next and tear your head straight off. \n The end.")
            quit()
        elif Input.lower() == "d":
            Document()
        else:
            print("Invalid response")
            continue   

#right side of the path
def Right():
    while True:
        abandoned_house = Image.open('house.jpg')
        abandoned_house.show()
        Input = input("Through the right path, you see a huge abandoned house.\nWould you like to enter(e) it or leave(l): ")
        if Input.lower() == "e":
            Enter()
        elif Input.lower() == "l":
            Leave()
        else:
            print("Invalid response")
            continue

#left side of the path
def Left():
    while True:
        Input = input("Through the left path, you find yourself at the bottom of a clif \nWould you like to climb it(c) or keep walking(w): ")
        if Input.lower() == "c":
            Climb()
        elif Input.lower() == "w":
            Walk()
        else:
            print("Invalid response")
            continue

#the beginning when the person wants to go "back"
def Start():
    while True:
        Input = input("You have reached a cross road spliting in two directions. \nWould you like to go right(r) of left(l): ")
        if Input.lower() == "r":
            Right()
        elif Input.lower() == "l":
            Left()
        else:
            print("Invalid response")
            continue

#Getting name without numbers (without using google)
def GetName():
    while True: 
        NumberInName = ()
        Name = input("What is your name? ")
        Name = [Char for Char in Name]
        for i in range(len(Name)):
            try:
                NumberInName = (int(Name[i]) + 1)
                print("Name must not include number. ")
                break
            except: TypeError
        if NumberInName != ():
            continue
        else:
            break
    return("".join(Name))

#Gets valid name without characters and prints it.
print(f"Welcome {GetName()} to chose your own adventure. ")
Start()
