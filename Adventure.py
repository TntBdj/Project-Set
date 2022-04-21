from turtle import right
from urllib import response


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

def Right():
    print ("the right side tok you down a deep long path to a abandonded house. Enter")

def Left():


#Gets valid name without characters and prints it.
print(f"Welcomee {GetName()} to chose your own adventure. ")

while True:
    Input = input("You have reached a cross road spliting in two directions. Would you like to go right(r) of left(l): ")
    if Input.lower() == "r":
        Right()
    elif Input.lower() == "l":
        Left()
    else:
        print("Invalid response")
        continue

