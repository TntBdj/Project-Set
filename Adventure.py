#since its a buch of functions calling functions the start is the end and the end is the start
def Walk():
    while True:
        Input = input("")
        if Input.lower() == "r":
            print("You take the risk and it pays off. You are now at the top of the clif")
            Walk()
        elif Input.lower() == "l":
            print("You realize this route was way too long and your arms get tired. your fingers slip and you fall to your death. \n The end.")
        else:
            print("Invalid response")
            continue     

def Climb():
    while True:
        Input = input("while climbing you see a short cut, but it's risky. \n would you like to take the risk(r) or keep going the long way(l): ")
        if Input.lower() == "r":
            print("You take the risk and it pays off. You are now at the top of the clif")
            Walk()
        elif Input.lower() == "l":
            print("You realize this route was way too long and your arms get tired. your fingers slip and you fall to your death. \n The end.")
        else:
            print("Invalid response")
            continue     

def Leave():
    while True:
        Input = input("You leave and keep following the path to the edge of a clif. would you like to jump(j) or go back(b): ")
        if Input.lower() == "j":
            print("Take the leap and fall all the way to the bottom. Your head smashed into the floor and explodes into a million pieces. \n The end.")
        elif Input.lower() == "b":
            Walk()
        else:
            print("Invalid response")
            continue       

def NoParties():
    while True:
        Input = input("you go outside the abandoned house and find yourself at the bottom of a cliff .\n would you like to climb it(c) or keep walking(w)")
        if Input.lower() == "c":
            Climb()
        elif Input.lower() == "w":
            Walk()
        else:
            print("Invalid response")
            continue       


def Document():
    while True:
        Input = input("you successfully document the new creatures and post your findings. Do you like parties? (y/n): ")
        if Input.lower() == "y":
            print("You get home, celebrate you findings and make millions. The end")
        elif Input.lower() == "n":
            NoParties()
        else:
            print("Invalid response")
            continue   
def Enter():
    while True:
        Input = input("Inside you find out the house is a filled with all sorts of creatures that have never been seen before\n would you like to kill(k) or document them for research(d): ")
        if Input.lower() == "k":
            print("you end up successfully killing half of them untill you get to a small cat looking creature. You let your guard down and tentacles from inside the cats mouth reach out grab your next and tear your head straight off. \n The end.")
        elif Input.lower() == "d":
            Document()
        else:
            print("Invalid response")
            continue   

def Right():
    while True:
        Input = input("Through the right path, you see a huge abandoned house.\n Would you like to enter(e) it or leave(l): ")
        if Input.lower() == "e":
            Enter()
        elif Input.lower() == "l":
            Leave()
        else:
            print("Invalid response")
            continue
def Left():
    while True:
        Input = input("Through the left path, you find yourself at the bottom of a clif \n would you like to climb it(c) or keep walking(w): ")
        if Input.lower() == "c":
            Climb()
        elif Input.lower() == "w":
            Walk()
        else:
            print("Invalid response")
            continue

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
print(f"Welcomee {GetName()} to chose your own adventure. ")

while True:
    Input = input("You have reached a cross road spliting in two directions. \n Would you like to go right(r) of left(l): ")
    if Input.lower() == "r":
        Right()
    elif Input.lower() == "l":
        Left()
    else:
        print("Invalid response")
        continue
