from PIL import Image

question_pic1 = Image.open('1+1.jpg')
question_pic2 = Image.open('6.jpg')
Answers = [2, 8, 18, 24, 72, 49, 9, 26, 3, 81]
Questions = ["1 + 1 = ", "10 - 2 = ", "2 * 9 = ", "72 % 3 = ", "(8 + 16) * 3 = ", "(89 - 92) * 7 = ", "6 / 2 (1 + 2 ) = ", "(17 - 6 / 2) + 4 * 3 = ", "4^3 - 61 = ", "6^4 / 4^2 = "]
Score = 0
def Quiz():
    for i in range (len(Questions)):
        if i == 0:
            question_pic1.show()
        elif i == 6:
            question_pic2.show()
        response = int(input(f"{Questions[i]} "))
        if response == (Answers[i]):
            print ("correct")
            global Score
            Score = Score + 1
        else:
            print ("wrong")
    print(f"You got {Score} right out of {len(Questions)}")
    print(f"You got a {(Score/len(Questions))*100}% on the quiz")
while True:
    Play = input("Would you like to start the quiz? (Yes or No): ")
    if Play.lower() == "yes":
        Quiz()
    elif Play.lower() == "no":
        break
    else:
        print ("Invalid Input")
