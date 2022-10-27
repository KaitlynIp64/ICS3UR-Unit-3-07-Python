#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program uses a compound boolean statement


def main():
    # this function uses a compound boolean statement

    # input
    age_num = input("Please enter your age: ")
    print("")

    # process & output
    try:
        age_num = int(age_num)
        print("That is a valid input.")

    except ValueError:
        print("That is not a valid input.")

    else:
        if age_num >= 25 and age_num <= 40:
            print("You are an acceptable age.")
        else:
            print("You are NOT an acceptable age.")


if __name__ == "__main__":
    main()
