#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to pick a number from 0-9
# and tells them if they got it right or wrong
# and asks them to keep playing until they get it right


import random

random = random.randint(1, 9)


def main():
    # This function makes the user guess a number from 0-9
    loop_counter = 0
    # input
    number = input("Guess my number (0-9): ")
    print("")

    # process
    for loop_counter in range(5):
        try:
            integer = int(number)
            if integer == random:
                # output
                print("")
                print("Correct!")
                break
            else:
                print("")
                print("Incorrect")
                if loop_counter == 4:
                    break
                else:
                    number = input("try again: ")
        except ValueError:
            print("Invalid input.")
    print("")
    print("Correct number is:{} ".format(random))
    print("thanks for playing!")


if __name__ == "__main__":
    main()
