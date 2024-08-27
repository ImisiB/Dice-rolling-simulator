import random

def roll_dice():
    
    dice = {
    1 : (
        "_______",
        "|  1  |",
        "|  O  |",
        "|_____|",
    ),
    2 : (
        "_______",
        "| O   |",
        "|  2  |",
        "|___0_|",
    ),
    3 : (
        "_______",
        "|O   3|",
        "|  0  |",
        "|___O_|",
    ),
    4 : (
        "_______",
        "|0   0|",
        "|  4  |",
        "|0___0|",
    ),
    5 : (
        "_______",
        "|O 5 O|",
        "|  0  |",
        "|O___O|",
    ),
    6 : (
        "_______",
        "|O O O|",
        "|  6  |",
        "|O_O_O|",
    )
    
}
    rolling_dice = input("Do you want to roll a dice? (yes/no): ")
    
    while rolling_dice.lower() == "yes".lower():
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        
        print("Dice rolled: {} and {}".format(dice_1,dice_2))
        print("\n".join(dice[dice_1]))
        print("\n".join(dice[dice_2]))
        
        rolling_dice = input(" Do you want to roll again? (yes/no): ")

roll_dice()

