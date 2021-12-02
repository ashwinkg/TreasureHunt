## https://ascii.co.uk/art/treasure
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************              
''')

print("Welcome to Treasure Island!!!")
print("Your mission is to find teh treasure")

direction = input('You\'re at a crossroad, where do you want to go? Type "left" or "right" \n').lower()

if direction != "left":
    print("You fell into a hole GAME OVER!!! ")
else:
    action=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" tp swim across \n').lower()
    if action !="wait":
        print("You got attacked by an angry trout GAME OVER!!!")
    else:
        door=input("Which door do you want to open Red, Blue,Yellow \n").lower()
        if door == "red":
            print("It's a room full of fire. GAME OVER!!!")
        elif door =="blue":
            print("You enter a room of beasts. GAME OVER!!!")
        elif door=="yellow":
            print(" You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. GAME OVER")
    

