import random


def roll_die(s, x) -> list:
    rolls = list()
    for i in range(x):
        rolls.append(random.randint(1, s))
    return rolls


if __name__ == '__main__':
    errors = 0
    while 1:
        try:
            sides = int(input("Sides: "))
            amount = int(input("Amount: "))
            print(roll_die(sides, amount))
        except ValueError:
            errors += 1
            if errors == 3:
                break
            print("Please enter only numbers")
    print("Too many errors. Goodbye")

