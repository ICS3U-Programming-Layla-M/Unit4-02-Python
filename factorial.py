#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 21, 2021
# This program asks the user to input a number and then
# calculates and displays the factorial of that number

# ask user to input a whole number
number_as_string = input("Enter a whole number: ")


def main():
    # define variables
    factorial = 1
    counter = 0

    try:
        # convert from string to integer
        number_as_int = int(number_as_string)

        if (number_as_int < 0):
            # check if number is negative
            print("{} is not a whole number.". format(number_as_int))
        elif (number_as_int == 0):
            # check if number is 0
            print("0! = 1")
        else:
            # calculate the factorial
            while True:
                counter = counter + 1
                factorial = factorial * counter
                print("Tracking {} times through loop.". format(counter))

                if (counter >= number_as_int):
                    break

            print("")
            # display the factorial of the number
            print("{0}! = {1}". format(number_as_int, factorial))

    except ValueError:
        # error message
        print("{} is not a whole number.". format(number_as_string))


if __name__ == "__main__":
    main()
