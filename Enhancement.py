def examine(item_description):
    """Examine an item in the current location.
        item_description: The description of the item to examine.
    """
    print(f"You examine {item_description}.")

    if item_description == "desk":
        print(
            "The desk is made of wood and has a series of drawers, all of which are empty. "
            "\n On top of the desk lies a large blotter pad.")
    elif item_description == "blotter":
        print("You notice that someone has scribbled 'HappyJoyee' in the corner of the blotter.")
    elif item_description == "metal door":
        print("The door is locked, seemingly by an alphanumeric keypad next to the handle.")
    else:
        print(f"You cannot examine {item_description}.")


def type_code(code):
    """Type a code on the alphanumeric keypad.
        code: The code to type on the keypad.
    """
    print(f"You type '{code}' on the keypad.")

    if code == "HappyJoyee":
        print("The lock behind the handle clunks open.")
    else:
        print("Nothing happens. The code seems incorrect.")
