# starting dialogue
starting_dialogue = """
-------------------------------------------------------------------------------------------------------

    Welcome to everyone who uses Number Factorial Finder. This is some info to you while using program :

    1. To exit, write letter exit or quit in number input
    2. Results are full number and the range of numbers are from 0 to 1558
    3. This program is made by "ThisIsParsa". Github account url -> https://github.com/ThisIsParsa/ , this ID will probably change in future.
    4. Copying content of this file is allowed to everyone, so enjoy using this.

"""

print(starting_dialogue)

# program base function
def program(entry_value = None):
    ev = entry_value
    non_exeption: bool = True

    # entry numeric checking zone
    try:
        int_ev = int(ev)

        # result for exceptions
        if int_ev < 0:
            print("There is No Factorial For Negetive Numbers.\n")
            non_exeption = False
        elif int_ev == 0:
            print(f"Factorial Result For 0 is : 1.\n")
            non_exeption = False
        elif int_ev >= 1559:
            print("OUT OF RANGE.\n")
            non_exeption = False

        # result for non exeptions
        if non_exeption:
            # assigning a base number to result variable
            result = 1

            # factorial finder algorithem
            for i in range(1, int_ev + 1):
                result = result * i
            print(f"Factorial Result For {ev} is : {result}.\n")

    except:
        print("Please Enter a Numeric Value.\n")


# creating a while loop to run program forever until exiting event triggered
while True:

    print("-------------------------------------------------------------------------------------------------------")

    # making an input to get number and assigning a variable to it
    entry_num_str = input("\nPlease Enter Number You Want > ")

    if entry_num_str.lower() == "exit" or entry_num_str.lower() == "quit":
        break

    program(entry_num_str)
