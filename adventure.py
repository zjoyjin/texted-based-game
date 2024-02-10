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

from game_data import Location, Player, Shop
from world import World
from puzzle import examine, look_closer


N, E, S, W = "NORTH", "EAST", "SOUTH", "WEST"


def get_directions(world: World, player: Player) -> list[str]:
    """ Return the possible movement directions from current location [N,S,E,W]
    """
    directions = []
    # North
    if world.get_location(player.x, player.y - 1) is not None:
        directions.append(N)
    # South
    if world.get_location(player.x, player.y + 1) is not None:
        directions.append(S)
    # East
    if world.get_location(player.x + 1, player.y) is not None:
        directions.append(E)
    # West
    if world.get_location(player.x - 1, player.y) is not None:
        directions.append(W)
    return directions


# Prompts for player:
def menu_prompt(player: Player) -> None:
    """ MENU prompt for the player.
    Also calls the appropriate function depending on player input.
    """
    print("Menu Options: ")
    for option in menu:
        print(option, end="\t")
    selection = input("\nChoose action: ").upper()
    if selection == "INVENTORY":
        player.display_inventory()
    elif selection == "MORALE":
        player.print_morale()
    elif selection == "TIME":
        player.print_steps()
    elif selection == "WALLET":
        player.display_balance()
    elif selection == "QUIT GAME":
        quit()
    elif selection != "BACK":
        print("Invalid input!")
        menu_prompt(player)


def move_prompt(world: World, player: Player) -> None:
    """ MOVE prompt for the player.
    Prints available movement directions, and calls functions to update player location and step count.
    """
    print("Where to go?")
    dirs = get_directions(world, player)
    for d in dirs:
        print(d, end="\t")
    print("BACK")
    direction = input("Enter direction: ").upper()
    if direction in dirs:
        player.move(direction)
        player.update_steps()
    elif direction != "BACK":
        print("Invalid direction!")
        move_prompt(world, player)


def drop_prompt(world: World, loc: Location, player: Player) -> None:
    """ DROP prompt for the player.
    Also calls functions that update player inventory and location.items accordingly.
    """
    selected_item = input("What item should be dropped? (enter 'BACK' to go back) ").title()
    item = world.get_item_from_name(selected_item)
    if item in player.inventory:
        if not item.key_item and loc.num != 39 and not isinstance(loc, Shop):
            player.drop(item)
            loc.add_item(item)
        elif item.key_item and loc.num == 39:
            player.take_out(item, True)
        else:
            print("Cannot drop this item here!")
    elif selected_item != "Back":
        print("Invalid item!")
        drop_prompt(world, loc, player)


def pick_up_prompt(world: World, player: Player, loc: Location) -> None:
    """ PICK UP prompt for the player.
    Also calls functions that update player inventory and location.items accordingly.
    """
    selected_item = input("\nPick up which item? (enter 'BACK' to go back) ").title()
    item = world.get_item_from_name(selected_item)
    if item in loc.items:
        player.pick_up(item)
        loc.remove_item(item)
    elif selected_item != 'Back':
        print("Invalid item!")
        pick_up_prompt(world, player, loc)


def buy_prompt(world: World, loc: Shop, player: Player) -> None:
    """ BUY prompt for the player. Can only be called if player is in a shop.
    Prints purchaseable items at location, and calls functions that update
    player inventory, player wallet, and location.items.
    """
    print(f"Welcome to {loc.name}!")
    loc.print_wares()
    selected_item = input("What to buy? (enter 'BACK' to go back) ").title()
    item = world.get_item_from_name(selected_item)
    if item in location.items:
        if player.wallet.buy(item.price):
            loc.sold(item)
            player.pick_up(item)
    elif selected_item != 'Back':
        print("Invalid item!")
        buy_prompt(world, location, player)


if __name__ == "__main__":

    with open('map.txt') as map_file, open('locations.txt') as location_file, open('items.txt') as item_file:
        w = World(map_file, location_file, item_file)
    p = Player(9, 1)
    menu = ["INVENTORY", "MORALE", "TIME", "BACK", 'WALLET', "QUIT GAME"]
    completed_puzzle = False

    while not p.check_victory():
        location = w.get_location(p.x, p.y)
        location.print_desc()
        if not isinstance(location, Shop):
            location.print_items()

        print("\nWhat to do?")
        print("MOVE\tLOOK\tMENU\tPICK UP    DROP ", end="\t")
        if location.npc:
            print("TALK", end="\t")
        if isinstance(location, Shop):
            print("BUY", end="\t")
        if location.num == 36 and not completed_puzzle:
            print("LOOK CLOSER\tEXAMINE", end="\t")

        choice = input("\nEnter action: ").upper()

        if choice == "MENU":
            menu_prompt(p)
        elif choice == "MOVE":
            if location.num != 36 or completed_puzzle:
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
        elif choice == "PICK UP":
            if location.get_items() and not isinstance(location, Shop):
                pick_up_prompt(w, p, location)
            else:
                print("There are no items to pick up.")
        elif choice == "TALK" and location.npc:
            npc = location.get_npc()
            if npc.name == "Miserable Student":
                npc.prompt(p, w.items)
            else:
                npc.prompt(p)
        elif choice == "BUY" and isinstance(location, Shop):
            buy_prompt(w, location, p)
        elif choice == "LOOK CLOSER" and location.num == 36 and not completed_puzzle:
            look_closer()
        elif choice == "EXAMINE" and location.num == 36 and not completed_puzzle:
            completed_puzzle = examine()
        else:
            print("Invalid option!")

        if p.steps > 150:
            p.print_steps()
            print("Oh no! You missed your exam... womp womp :(")
            break

    # Check for victory (2 different endings!)
    if p.morale >= 20:
        print("You made it to the exam centre will all your material! \
              Despite all the stress and the struggle, you feel confident and ready. Good luck!")
    elif p.check_victory():
        print("Despite your exhaustion, you made it to the exam centre will all your material. \
              But your morale is too low that you can't take the exam. You can go home and sleep.")
