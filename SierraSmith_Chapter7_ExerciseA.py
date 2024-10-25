# Virtual Journal Program
# In this program, you can write any number of sentences beginning with letters
# or numbers. When you finish, the program will display all the sentences
# you entered and the number of sentences you wrote.

import re
import time


DIV = "---" * 25

# first function to be called, contains every other function in the program
def main():


    print(DIV)

    # welcome message
    print("Welcome to your Virtual Journal.")

    write()



# function that takes user input, matches it with a regular expression pattern,
# and displays it all as individually numbered sentences.
def write():


    # regular expression pattern
    pat1 = r'\w.*?[.!?] |\w.*?[.!?]'

    time.sleep(.7)

    # user input that will be scanned for matches
    entry = input("What's on your mind? Press ENTER when finished: ")

    # expression that finds all matches in the entry by comparing it with the regex pattern.
    # every match that is found is saved to "lines"
    lines = re.findall(pat1, entry, flags=re.DOTALL)


    # count representing how many sentences are in the user input
    count = 0

    print(DIV)

    # success message
    print("Entry logged successfully! Here is what you typed:\n")

    # each sentence submitted by the user is numbered and displayed
    for i in lines:
        count += 1

        print(f"{count}. {i}")

    # displays the total number of sentences that were recorded
    print(f"\nTotal sentences: {count}\n")


    another()



# function for user to choose to write another entry or exit the program
def another():


    print(f"That concludes your entry.")
    print(DIV)

    # determining input that restarts program or exits it
    yes = input("Want to write some more? Enter X to exit or a different key for yes: ")

    if yes == "x" or yes == "X":

        exit()

    else:

        write()



# call main function
main()