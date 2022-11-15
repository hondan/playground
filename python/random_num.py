#! /usr/bin/env python -tt
'''
This is a short little code snippit that demonstrates the random integer generator function.
'''

from random import randint


def main():
    # Introduction and get user input until an integer is obtained
    print("++ This program will generate random numbers ++\n")
    error = 1
    while error == 1:
        try:
            minnum = int(input("Please enter the minimum value: "))
            maxnum = int(input("Please enter the maximum value: "))
            error = 0
        except Exception:
            print("\nPlease only enter integers...\n")
            pass

    # Make sure min is less than max, then pick and display value.
    if maxnum > minnum:
        print(f"\nThe number I picked between {str(minnum)} and {str(maxnum)} is {str(randint(minnum,maxnum))}")
    else:
        print(f"\nThere are some problems with {str(minnum)} and {str(maxnum)}, please make sure the minimum value "
              f"is less than the maximum value")


if __name__ == "__main__":
    main()
