"""
This file containes functions related to the puzzle to be completed by the player
on Robarts F1.
"""


def look_closer() -> None:
    """ Print a more detailed description of the first floor of robarts
    """
    print("Upon closer inspection, it is not as if there is no sign of life whatsoever. ",
          "Some chairs were left unpushed, away from their desks, while others are covered in faint grains ",
          "you assume are crumbs. The nearest desk even has a pen and a blotter pad, as well as an ",
          "abandoned mint tin. Strangely enough, a metal door is blocking the way to the second floor.")


def examine() -> bool:
    """ Lets player get the description of an object in F1 robarts.
        Returns if the puzzle has been completed or not (whether the code typed is correct).
    """
    choice = input("What should be examined? (enter 'BACK' to go back) ").lower()

    if choice == "desk":
        print("The desk is made of wood and has a series of drawers, all of which are empty. ",
              "On top of the desk lies a large blotter pad.")
    elif choice in {"blotter", "blotter pad"}:
        print("You notice that someone has scribbled 'HappyJoyee' in the corner of the blotter.")
    elif choice == "chair":
        print("The chair is turned away from the desk. A wheel is missing.")
    elif choice == "crumbs":
        print("They appear to be from the nachos sold on the second store.")
    elif choice == "mint tin":
        print("They're green tea mints from Trader Joe's. Are there even Trader Joe's' in Canada?")
    elif choice == "metal door":
        print("The door is locked by an alphanumeric keypad next to the handle.")
        return type_code()
    elif choice != "back":
        print(f"You cannot examine {choice}.")
        return examine()
    return False


def type_code() -> bool:
    """Type a code on the alphanumeric keypad.
        code: The code to type on the keypad.
        Returns whether or not the code is correct.
    """
    code = input("Input code: ")

    if code == "HappyJoyee":
        print("The lock behind the handle clunks open.")
        return True
    else:
        print("Nothing happens. The code seems incorrect.")
        return False
