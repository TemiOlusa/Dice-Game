import random

def get_input():
    while True:
        try:
            user_Input = int(input("Would you like to roll 1 or 2 dice: "))
            if user_Input in [1, 2]:
                return user_Input
            else:
                print("Error 15: Please Select from the available list")
        except ValueError as e: 
            print("Error 419: ", e)


def roll_Dice(dice_Number):
    for i in range(1, dice_Number + 1):
        dice = random.randint(1, 6)
        print(f"Dice {i} landed on {dice}")


#Main Loop
while True:
    dice_Number = get_input() 
    print("Welcome to the Dice game")
    roll_Dice(dice_Number)

    reroll = input("Would you like to roll again: Yes or No\n").strip().lower()
    if reroll in ["no", "n"]:
        print("Exiting ...")
        break
    elif reroll == ["yes", "y"]:
        print("Rebooting...")
        continue
    else:
        print("Invalid choice, rebooting...")
        