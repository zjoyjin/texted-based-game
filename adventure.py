"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
# Note: You may add in other import statements here as needed
from game_data import Item, Location, Player
from world import World

N, E, S, W = "NORTH", "EAST", "SOUTH", "WEST"   #move into get_directions if not needed

# Note: You may add helper functions, classes, etc. here as needed
def get_directions() -> list:
    """ return the possible movement directions from current location [N,S,E,W]
    """
    directions = []
    # North
    if w.get_location(p.x, p.y - 1) is not None:
        directions.append(N)
    #South
    if w.get_location(p.x, p.y + 1) is not None:
        directions.append(S)
    #East
    if w.get_location(p.x + 1, p.y) is not None:
        directions.append(E)
    #West
    if w.get_location(p.x - 1, p.y) is not None:
        directions.append(W)
    return directions

#TODO
def update_location_items():
    pass

def menu_prompt():
    print("Menu Options:")
    for option in menu:
        print(option, "\t")
    choice = input("\nChoose action: ").upper()
    if choice == "INVENTORY":
        p.display_inventory()
    elif choice == "MORALE":
        print(p.print_morale())
    elif choice == "TIME":
        print(p.print_steps())
    elif choice == "QUIT GAME":
        quit()
    elif choice != "BACK":
        print("Invalid input!")
        menu_prompt()

def move_prompt():
    print("Where to go?")
    dirs = get_directions()
    for dir in dirs:
        print(dir, "\t")
    print("BACK")
    choice = input("Enter direction: ").upper()
    if choice in dirs:
        p.move(choice)
    elif choice != "BACK":
        print("Invalid direction!")
        move_prompt()

def drop_prompt():
    selected_item = input("What item should be dropped? (enter 'BACK' to go back) ").upper()
    item = w.get_item_from_name(selected_item)
    if item:
        p.drop(item)
    elif selected_item != "BACK":
        print("Invalid item!")
        drop_prompt()

def pick_up_prompt():
    item_names = {}
    for item in location.items:
        item_names.add(item.name)
        print(item.name, "\t")
    selected_item = w.input("\nPick up which item? (enter 'BACK' to go back) ").title()
    if selected_item in item_names:
        p.pick_up(w.get_item_from_name(selected_item))
        #TODO: UPDATE ITEMS VAR FOR LOCATION
    elif selected_item != 'Back':
        print("Invalid item!")
        pick_up_prompt()

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    with open('map.txt') as map_file, open('locations.txt') as location_file, open('items.txt') as item_file:
        w = World(map_file, location_file, item_file)
    
    p = Player(0, 0)  # set starting location of player; you may change the x, y coordinates here as appropriate


    menu = ["INVENTORY", "MORALE", "TIME", "BACK", "QUIT GAME"]

    while not p.victory:
        location = w.get_location(p.x, p.y)
        if location.visited:
            print(location.short_desc)
        else:
            print(location.long_desc)

        print("What to do?")
        print("MOVE\tLOOK\tPICK UP\tDROP\tMENU")

        # for action in location.available_actions():
        #     print(action)
        choice = input("\nEnter action: ").upper()

        if choice == "MENU":
            menu_prompt()
        elif choice == "MOVE":
            move_prompt()
        elif choice == "LOOK":
            print(location.long_desc)
        elif choice == "DROP":
            drop_prompt()
        elif choice == "PICK UP":
            if location.items:
                pick_up_prompt()
            else:
                print("There are no items to pick up.")



        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
