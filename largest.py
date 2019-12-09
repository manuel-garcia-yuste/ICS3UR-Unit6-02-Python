# !/usr/bin/env python3

# Created by: Manuel
# Created on: December 2019
# This program generate random number and find the largest

import random


def largest_number(numbers):

    last_number = 0

    for number in numbers:
        if number > last_number:
            largest = number
            last_number = number

    return largest


def main():
    # Input
    largest = 0

    numbers = []

    # process
    for repeater in range(0, 10):
        number = random.randint(0, 100)
        numbers.append(number)

        print(numbers[repeater])
    largest = largest_number(numbers)

    # output
    print("The largest number is " + str(largest))


if __name__ == "__main__":
    main()
