"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        # TODO: Complete this method
        self.x = -1
        self.y = -1
        short = ''
        long = ''
        commands = []
        N, E, S, W = "North", "East", "South", "West"

    def available_actions(self):
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        # TODO: Complete this method, if you'd like or remove/replace it if you're not using it
    def get_directions(self) -> list:
        """ return the possible movement directions from current location [N,S,E,W]
        """


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """


    def __init__(self, name: str, start: int, target: int, target_points: int, price: int, x:int, y:int, key_item: bool) -> None:
        """Initialize a new item.
        """


        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class
        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points
        self.price = price
        self.x = x
        self.y = y
        self.key_item = key_item

class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - inventory: the player's inventory
        -

    Representation Invariants:
        - self.Inventory >= []
    """
    inventory: []
    vicotry :bool
    score :int
    wallet: int




    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.score =0
        self.location = (x, y)


    # def move(self, dx, dy):
    #     self.x += dx
    #     self.y += dy
    # def move(self, direction: int, dx, dy) -> None:
    #     """Move the player to a new room based on the specified direction.
    #     """
    #     self.x += dx
    #     self.y += dy
    #     new_position = self.current_room.position + direction
    #     if new_position == -1:
    #         print("You can't go beyond this point.")
    #     else:
    #         for room in self.world:
    #             if room.position == new_position:
    #                 self.current_room = room
    #                 print(f"You move to {room.name}.")
    #                 return
    #         print("Invalid direction.")
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def print_score(self, score):
        print(f"Your score is {self.score}")

    def display_inventory(self) -> None:
        """Display the items in the player's inventory.
        """
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for item in self.inventory:
                print(item)

    def pick_up(self, item):
        """Add an item to the player's inventory.
            item: The item to add to the inventory.
        """
        self.inventory.append(item)
        print(f"You picked up {item}.")

    def take_out(self, item):
        """Remove an item from the player's inventory.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You took out {item} from your inventory.")
        else:
            print(f"{item} is not in your inventory.")

    def drop(self, item, location):
        """Drop an item from the player's inventory at a specified location
            item: The item to drop from the inventory.
            location: The location where the item is dropped.
        """
        if item in self.inventory:
            self.inventory[item] = self.location
            print(f"You dropped {item} at {location}.")
        else:
            print(f"{item} is not in your inventory, so you cannot drop it.")


class Wallet:
    """Player's wallet in the text adventure game.

    Instance Attributes:
        - money (int): The amount of money in the wallet.
    """

    def __init__(self, initial_money: int) -> None:
        """Initialize the wallet with an initial amount of money.
        """
        self.money = 100

    def display_balance(self) -> None:
        """Display the current balance in the wallet.
        """
        print(f"Wallet Balance: ${self.money}")

    def buy(self, amount: int) -> bool:
        """Attempt to buy an item and deduct the specified amount from the wallet.
        Returns:
            bool: True if the purchase is successful, False otherwise.
        """
        if self.money >= amount:
            self.money -= amount
            print(f"Purchase successful! ${amount} deducted from your wallet.")
            return True
        else:
            print("Insufficient funds. Purchase failed.")
            return False

def helper_wallet():
    # Example usage
    player_wallet = Wallet(initial_money=50)
    player_wallet.display_balance()

    # Attempt to buy an item costing $30
    if player_wallet.buy(30):
        player_wallet.display_balance()
    else:
        print("Failed to make the purchase.")

    # Attempt to buy another item costing $60
    if player_wallet.buy(60):
        player_wallet.display_balance()
    else:
        print("Failed to make the purchase.")


class NPC:
    """Base class for Non-Playable Characters (NPCs) in the text adventure game.

    Instance Attributes:
        - name (str): The name of the NPC.
        - happiness (int): The happiness level of the NPC.
        - money (int): The amount of money the NPC has.
        - score (int): The score or morale of the NPC.
    """

    def __init__(self, name: str, happiness: int, money: int, score: int) -> None:
        """Initialize a new NPC.
        """
        self.name = name
        self.happiness = happiness
        self.money = money
        self.score = score

    def talk(self) -> None:
        """NPC talks."""
        print(f"{self.name} says: Hello! How are you today?")
        self.happiness += 1
        self.check_happiness()

    def rob(self, player) -> None:
        """Player attempts to rob the NPC."""
        print(f"You attempt to rob {self.name}.")
        if self._rob_attempt():
            print(f"You successfully rob {self.name}!")
            player.money += self.money
            self.money = 0
            self.score -= 5
        else:
            print(f"Your robbery attempt on {self.name} fails!")
            player.score -= 2

    def leave(self) -> None:
        """NPC leaves."""
        print(f"{self.name} says goodbye and leaves.")

    def _rob_attempt(self) -> bool:
        """Simulate a robbery attempt."""
        # Override this method in subclasses to customize robbery behavior.
        return False

    def check_happiness(self) -> None:
        """Check happiness and reward running shoes if happiness exceeds a threshold."""
        if self.happiness > 5:
            print(f"{self.name} is very happy! They give you a pair of running shoes.")
            # Give running shoes (you can add the logic to create an Item object here)

# Subclasses????

class RichLady(NPC):
    """A rich lady NPC."""

    def _rob_attempt(self) -> bool:
        """Robbery attempt for RichLady (always succeeds)."""
        return True

    def harass_player(self, player) -> None:
        """RichLady harasses the player."""
        print(f"{self.name} looks at you with sideeyes and says: What are you doing here? You don't belong!")
        print("Options:")
        print("1. Respond calmly.")
        print("2. Insult her back.")
        print("3. Attempt to rob her.")
        print("4. Leave.")

        choice = input("Enter your choice (1, 2, 3, or 4): ")
        if choice == '1':
            print("You respond calmly and try to defuse the situation.")
            player.happiness += 2
        elif choice == '2':
            print("You insult her back, but it only escalates the situation.")
            player.happiness -= 3
        elif choice == '3':
            print("You decide to attempt to rob her in response to the harassment.")
            self.rob_player(player)
        elif choice == '4':
            print("You decide to leave to avoid further confrontation.")
        else:
            print("Invalid choice. You decide to leave.")

class CryingGirl(NPC):
    """A crying girl NPC."""

    def __init__(self, name: str, happiness: int, money: int, score: int, has_baby_rock: bool = False) -> None:
        """Initialize a new CryingGirl.
        """
        self.has_baby_rock = has_baby_rock

    def _rob_attempt(self) -> bool:
        """Robbery attempt for CryingGirl (always fails)."""
        return False

    def request_baby_rock(self, player) -> None:
        """CryingGirl talks to the player and requests them to find a baby rock."""
        print(f"{self.name} is crying and says: Oh dear, could you please find a baby rock for me? It means a lot.")
        print("Options:")
        print("1. Find the baby rock.")
        print("2. Leave.")

        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            self.find_baby_rock(player)
        elif choice == '2':
            print("You decide to leave.")
        else:
            print("Invalid choice. You decide to leave.")

    def find_baby_rock(self, player) -> None:
        """Player finds the crying girl's baby rock."""
        if not self.has_baby_rock:
            print(f"You find a baby rock near {self.name}.")
            player.inventory.append("Baby Rock")
            self.has_baby_rock = True
            player.happiness += 3
            print("You feel a sense of accomplishment and gain happiness!")
        else:
            print(f"You've already found the baby rock near {self.name}.")
            player.happiness += 1
            print("You feel a bit happier!")



class MiserableStudent(NPC):
    """A miserable student NPC."""

    def __init__(self, name: str, happiness: int, money: int, score: int, has_food: bool = False) -> None:
        """Initialize a new MiserableStudent.
        """
        self.has_food = has_food
    def _rob_attempt(self) -> bool:
        """Robbery attempt for MiserableStudent (always succeeds)."""
        return True

    def ask_for_food(self, player) -> None:
        """MiserableStudent talks to the player about finals and asks for food."""
        print(
            f"{self.name} looks stressed and says: I have final exams coming up, and I'm starving. Can you buy me some food from the 7-Eleven store?")

        # Check if the player has already bought food for the student
        if self.has_food:
            print("You've already bought food for the student. They look grateful.")
            player.happiness += 2
        else:
            print("Options:")
            print("1. Agree to buy food and go to the 7-Eleven store.")
            print("2. Refuse and leave.")

            choice = input("Enter your choice (1 or 2): ")
            if choice == '1':
                self.go_to_store(player)
            elif choice == '2':
                print("You decide to refuse and leave.")
            else:
                print("Invalid choice. You decide to leave.")

    def go_to_store(self, player) -> None:
        """Player goes to the 7-Eleven store to buy food."""
        print("You need to go to the 7-Eleven store.")

        # Assume the player can buy food for $5
        if player.money >= 5:
            print("You buy some food for the miserable student.")
            self.has_food = True
            player.money -= 5
            player.inventory.append("Food")
            player.happiness += 3
            print("You've successfully bought food for the student, and they look grateful.")
        else:
            print("You don't have enough money to buy food. The student continues to look hungry.")








class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - # TODO add more instance attributes as needed; do NOT remove the map attribute

    Representation Invariants:
        - # TODO
    """
    locations = [None]*23
    items = []

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.locations = self.load_locations(location_data)
        self.items = self.load_items(items_data)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        return [line.split() for line in map_data]

    # TODO: Add methods for loading location data and item data (see note above).
    # TODO: sort out actions (nested actions?)
    def load_locations(self, location_data: TextIO):
        current = []    # contains data for one location -- number, name, x, y, short desc, long desc, 
        for line in location_data:  # in numerical order (location 0 = locations[0])
            if 'LOCATION' in line:
                current.append[int(line.split()[1])]
            elif line == '\n':
                self.locations[current[0]] = Location(current[0], current[1], self.get_location_coords(current[0]), current[2], current[3])
                current = []
            else:
                current.append(str(line))
    
    def load_items(self, item_data: TextIO):
        for line in item_data:
            current = line.split(',')
            self.items.append(Item[current[4], self.get_location(current[0], current[1]).num, current[2], current[3]])

    def get_location_coords(self, num):
        for y in range(13):
            for x in range(11):
                if self.location[y][x] == num:
                    return (x, y)
        return None

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """

        # Complete this method as specified. Do not modify any of this function's specifications.
        num = self.map[y][x]
        if num == -1:
            return None
        return self.locations[num]
    
