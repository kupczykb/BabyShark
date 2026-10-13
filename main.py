"""----------------------------------------------------------------
Name:       Brayden Kupczyk
Assignment: Lab - Baby Shark
Course:     CS 1430, Section Online, Fall 2026
Purpose:    This program is designed to be practice for Python
            functions

Input: None

Output: The sound Baby Shark, with three verses:
        Baby Shark,
        doo-doo-doo-do-do-do-do *3
        Baby Shark!
        Mommy Shark,
        doo-doo-doo-do-do-do-do *3
        Mommy Shark!
        Daddy Shark,
        doo-doo-doo-do-do-do-do *3
        Daddy Shark!
----------------------------------------------------------------"""

##############
# CONSTANTS
##############
REPEAT = 3

def print_line(character):
    for _ in range(REPEAT):
        print(character,"Shark,")
        print("doo-doo-doo-do-do-do-do")
    print(character,"Shark!")

def main():
    print_line("Baby")
    print_line("Mommy")
    print_line("Daddy")

if __name__ == "__main__":
    main()
