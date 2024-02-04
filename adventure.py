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
from game_data import Item, Location, Player, Shop, Wallet
from world import World
from puzzle import examine, type_code

from python_ta.contracts import check_contracts

N, E, S, W = "NORTH", "EAST", "SOUTH", "WEST"  # move into get_directions if not needed
from puzzle import examine, type_code, look_closer



# Note: You may add helper functions, classes, etc. here as needed
def get_directions(w: World, p: Player) -> list:
    """ return the possible movement directions from current location [N,S,E,W]
    """
    directions = []
    # North
    if w.get_location(p.x, p.y - 1) is not None:
        directions.append(N)
    # South
    if w.get_location(p.x, p.y + 1) is not None:
        directions.append(S)
    # East
    if w.get_location(p.x + 1, p.y) is not None:
        directions.append(E)
    # West
    if w.get_location(p.x - 1, p.y) is not None:
        directions.append(W)
    return directions


# Updating items and init npc in Location Class
def add_item_to_loc(location: Location, item: Item):
    location.add_item(item)


def remove_item_from_loc(location: Location, item: Item):
    location.remove_item(item)


def init_items_and_npc_to_loc(w: World):
    for item in w.items:
        for location in w.locations:
            if (item.x, item.y) == (location.x, location.y):
                add_item_to_loc(location, item)
    for npc in w.npcs:
        for location in w.locations:
            if (npc.x, npc.y) == (location.x, location.y):
                location.add_npc(npc)


# Prompts for player:
def menu_prompt(p: Player):
    print("Menu Options:")
    for option in menu:
        print(option, "\t")
    choice = input("\nChoose action: ").upper()
    if choice == "INVENTORY":
        p.display_inventory()
    elif choice == "MORALE":
        p.print_morale()
    elif choice == "TIME":
        p.print_steps()
    elif choice == "WALLET":
        p.display_balance()
    elif choice == "QUIT GAME":
        quit()
    elif choice != "BACK":
        print("Invalid input!")
        menu_prompt(p)

def move_prompt(w: World, p: Player):
    print("Where to go?")
    dirs = get_directions(w, p)
    for dir in dirs:
        print(dir, "\t")
    print("BACK")
    choice = input("Enter direction: ").upper()
    if choice in dirs:
        p.move(choice)
        p.update_steps()
    elif choice != "BACK":
        print("Invalid direction!")
        move_prompt(w, p)

def drop_prompt(w: World, location: Location, p: Player):
    selected_item = input("What item should be dropped? (enter 'BACK' to go back) ").title()
    item = w.get_item_from_name(selected_item)
    if item in p.inventory:
        if not item.key_item and location.num != 39 and not isinstance(location, Shop):
            p.drop(item)
            add_item_to_loc(location, item)
        elif item.key_item and location.num == 39:
            p.take_out(item, True)
        else:
            print("Cannot drop this item here!")
    elif selected_item != "Back":
        print("Invalid item!")
        drop_prompt(w, location, p)

def pick_up_prompt(w: World, p: Player):
    selected_item = input("\nPick up which item? (enter 'BACK' to go back) ").title()
    item = w.get_item_from_name(selected_item)
    if item in location.items:
        p.pick_up(item)
        remove_item_from_loc(location, item)
    elif selected_item != 'Back':
        print("Invalid item!")
        pick_up_prompt(w, p)

def robarts_first_floor_puzzle(p: Player, location: Location):
    """Checks if the player is at the specified location and triggers the Robarts Library puzzle.
        player_location: The current location of the player.
    """
    examine()

def buy_prompt(location: Shop, p: Player):
    print(f"Welcome to {location.name}!")
    location.print_wares()
    selected_item = input("What to buy? (enter 'BACK' to go back)").title()
    item = w.get_item_from_name(selected_item)
    if item in location.items:
        p.wallet.buy(item.price)
        p.pick_up(item)
    elif selected_item != 'Back':
        print("Invalid item!")
        buy_prompt(location, p)


# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    with open('map.txt') as map_file, open('locations.txt') as location_file, open('items.txt') as item_file:
        w = World(map_file, location_file, item_file)
    p = Player(9, 1)  # set starting location of player; you may change the x, y coordinates here as appropriate
    menu = ["INVENTORY", "MORALE", "TIME", "BACK", 'WALLET', "QUIT GAME"]

    while not p.check_victory():
        location = w.get_location(p.x, p.y)
        location.print_desc()
        if not isinstance(location, Shop):
            location.print_items()

        print("\nWhat to do?")
        print("MOVE\tLOOK\tMENU\tPICK UP\t\tDROP", "\t")
        if location.npc:
            print("TALK", "\t")
        if isinstance(location, Shop):
            print("BUY", "\t")
        if location.num == 36 and not p.completed_puzzle:
            print("LOOK CLOSER\tEXAMINE ITEM", "\t")

        choice = input("\nEnter action: ").upper()

        if choice == "MENU":
            menu_prompt(p)
        elif choice == "MOVE":
            if location.num != 36 or p.completed_puzzle:
                move_prompt(w, p)
            # vv to restrict 2nd floor robarts access before puzzle completion
            else:
                print("Where to go?")
                print("EAST\tBACK")
                choice = input("Enter direction: ").upper()
                if choice == "EAST":
                    p.move(choice)
                    p.update_steps()
                elif choice != "BACK":
                    print("Invalid direction!")
                    move_prompt(w, p)
        elif choice == "LOOK":
            print(location.long_desc)
        elif choice == "DROP":
            drop_prompt(w, location, p)

        # NOTE: change v for the puzzle and stuff
        elif choice == "PICK UP":
            if location.get_items() and not isinstance(location, Shop):
                pick_up_prompt(w, p)
            else:
                print("There are no items to pick up.")
        elif choice == "TALK" and location.npc:
            npc = location.get_npc()
            if npc.name == "Miserable Student":
                npc.prompt(p, w.items)
            else:
                npc.prompt(p)
        elif choice == "BUY" and isinstance(location, Shop):
            buy_prompt(location, p)
        elif choice == "LOOK CLOSER" and location.num == 36 and not p.completed_puzzle:
            look_closer()
        elif choice == "EXAMINE OBJECT" and location.num == 36 and not p.completed_puzzle:
            examine(p)
        else:
            print("Invalid option!")

        # Check loss
        if p.steps > 560:
            p.print_steps()
            print("Oh no! You missed your exam... womp womp :(")

        # Check for victory
    if p.morale >= 0:
        print(
            "You made it to the exam centre will all your material! Despite all the stress and the struggle, you feel confident and ready. Good luck!")
    else:
        print(
            "Despite your exhaustion, you made it to the exam centre will all your material. You just have to get through one last challenge before you can go home and sleep... Good luck!")

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
        # import python_ta
        #
        # python_ta.check_all(config={
        #     'max-line-length': 120
        # })



