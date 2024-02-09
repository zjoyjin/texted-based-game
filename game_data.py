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
from typing import Optional
from python_ta.contracts import check_contracts


@check_contracts
class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """
    name: str
    x: Optional[int]        # None if in inventory
    y: Optional[int]
    price: int
    key_item: bool

    def __init__(self, name: str, price: int, location: tuple, key_item: str) -> None:
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
        self.x = location[0]
        self.y = location[1]
        self.price = price
        if key_item == "False":
            self.key_item = False
        else:
            self.key_item = True

    def update_location(self, x: Optional[int], y: Optional[int]) -> None:
        """ Update position of item. None if in inventory.
        """
        self.x = x
        self.y = y


@check_contracts
class Wallet:
    """Player's wallet in the text adventure game.

    Instance Attributes:
        - money (int): The amount of money in the wallet.
    """
    money: int

    def __init__(self) -> None:
        """Initialize the wallet with an initial amount of money.
        """
        self.money = 100

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

    def earn(self, amount: int) -> None:
        self.money += amount


@check_contracts
class Player:
    """
    A Player in the text advanture game.
    Instance Attributes:
        - inventory: the player's inventory
        - x: the player's x coordinates
        - y: the player's y coordinates
        - wallet: the player's wallet
        - morale: the player's morale
        - step: the total number of step the player is taking
        - has_running_shoes: if player have running shoes or not
        - completed_puzzle: if player have completed the puzzle

    Representation Invariants:
        - self. inventory >= []
        - self. wallet >=0
        - self. steps >=0

    """
    x: int
    y: int
    inventory: list[Item]
    wallet: Wallet
    morale: int
    steps: int
    _deposited: set[Item]  # for key items
    has_running_shoes: bool
    completed_puzzle: bool

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.
        # morale is equivalent to score

        self.x = x
        self.y = y
        self.inventory = []
        self.wallet = Wallet()
        self.morale = 0
        self.steps = 0
        self._deposited = set()  # for key items
        self.has_running_shoes = False
        self.completed_puzzle = False

    def move(self, dir: str) -> None:  # check for out of bounds in adventure.py
        if dir == "NORTH":
            self.y -= 1
        elif dir == "SOUTH":
            self.y += 1
        elif dir == "EAST":
            self.x += 1
        elif dir == "WEST":
            self.x -= 1

    def print_morale(self) -> None:
        print(f"Your morale is {self.morale}")

    def display_inventory(self) -> None:
        """Display the items in the player's inventory.
        """
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for item in self.inventory:
                print(item.name, ",", " ")

    def print_steps(self) -> None:
        print(f"It is {8 + self.steps // 60}: {self.steps % 60}. Your exam starts at 5:30!")

    def pick_up(self, item: Item) -> None:
        """Add an item to the player's inventory.
            item: The item to add to the inventory.
        """
        self.inventory.append(item)
        item.update_location(None, None)
        print(f"You picked up {item.name}.")

    def take_out(self, item: Item, at_ex: bool) -> None:  # at_ex: if we are at exam centre
        """Remove an item from the player's inventory.
        Precondition:
            - item in self.inventory
        """
        # giving to miserable student:
        if not at_ex and not item.key_item:
            self.inventory.remove(item)
            print(f"You took out {item.name} from your inventory.")
        # depositing at exam centre:
        elif at_ex and item.key_item:
            self.inventory.remove(item)
            self._deposited.add(item)
            self.morale += 5
            print(f"Deposited {item.name} at the Exam Centre!")
        else:
            print(f"Could not take out {item.name}.")

    def drop(self, item: Item) -> None:
        """Drop an item from the player's inventory at a specified location
            item: The item to drop from the inventory.
            location: The location where the item is dropped.
            NOTE: PLEASE DONT LET THEM DROP AT EXAM CENTRE
        """
        self.inventory.remove(item)
        item.update_location(self.x, self.y)
        if item.name == "Running Shoes":
            self.has_running_shoes = False
        print(f"You dropped {item.name}.")

    def display_balance(self) -> None:
        """Display the current balance in the wallet.
        """
        print(f"Wallet Balance: ${self.wallet.money}", "\t")

    def update_steps(self) -> None:
        if self.has_running_shoes:
            self.steps += 1
        else:
            self.steps += 2

    def got_running_shoes(self) -> None:
        self.has_running_shoes = True

    def check_victory(self) -> bool:
        if len(self._deposited) == 3 and self.steps <= 570:
            return True
        return False


@check_contracts
class NPC:
    """Base class for Non-Playable Characters (NPCs) in the text adventure game.

    Instance Attributes:
        - name (str): The name of the NPC.
        - happiness (int): The happiness level of the NPC.
        - money (int): The amount of money the NPC has.
        - morale (int): The morale or morale of the NPC.

     Representation Invariants:
     - self. name >= ' '
     - self. money >= 0
    """
    name: str
    money: int
    x: int
    y: int

    def __init__(self, name: str, money: int, x: int, y: int) -> None:
        """Initialize a new NPC.
        """
        self.name = name
        self.money = money
        self.x = x
        self.y = y

    # def talk(self) -> None:
    #     """NPC talks."""
    #     print(f"{self.name} says: Hello! How are you today?")

    def get_robbed(self, player: Player) -> None:
        """Player attempts to rob the NPC."""
        print(f"You attempt to rob {self.name}.")
        if self._rob_attempt() and self.money > 0:
            print(f"You successfully rob {self.name}!")
            player.wallet.earn(self.money)
            self.money = 0
            player.morale -= 5
        else:
            print(f"Your robbery attempt on {self.name} fails!")
            player.morale -= 5

    def leave(self) -> None:
        """NPC leaves."""
        print(f"{self.name} says goodbye and leaves.")

    def _rob_attempt(self) -> bool:
        """Simulate a robbery attempt."""
        # Override this method in subclasses to customize robbery behavior.
        return False

    def prompt(self, player: Player, items: [Item]) -> None:
        pass


@check_contracts
class RichLady(NPC):
    """A rich lady NPC."""

    def _rob_attempt(self) -> bool:
        """Simulate a robbery attempt."""
        # Override this method in subclasses to customize robbery behavior.
        return True

    def prompt(self, player: Player) -> None:
        """RichLady harasses the player."""
        print(f"{self.name} looks at you with sideeyes and says: What are you doing here? You don't belong!")
        print("Options: RESPOND\tINSULT\tROB\tLEAVE")

        choice = input("What to do? ").lower()
        if choice == 'respond':
            print("You respond calmly and try to defuse the situation. The lady sniffs disdainfully, but says nothing.")
            player.morale += 2
        elif choice == 'insult':
            print("You insult her back, but it doesn't helps the situation.")
            player.morale -= 3
        elif choice == 'rob':
            print("You decide to attempt to rob her.")
            self.get_robbed(player)
        elif choice == 'leave':
            print("You decide to leave to avoid further confrontation.")
        else:
            print("Invalid choice. You decide to leave.")


@check_contracts
class CryingGirl(NPC):
    """A crying girl NPC."""

    has_baby_rock: bool = False

    def _rob_attempt(self) -> bool:
        """Robbery attempt for CryingGirl (always fails)."""
        return False

    def prompt(self, player: Player) -> None:
        """CryingGirl talks to the player and requests them to find a baby rock."""
        print(f"{self.name}: *Sob* Oh dear, oh dear... Could you please find a baby rock for me? It means a lot. *Sob*")
        print("Options: GIVE BABY ROCK    ROB\tLEAVE")

        choice = input("What to do? ").lower()
        if choice == 'give baby rock':
            self.give_baby_rock(player)
        elif choice == 'rob':
            print("You decide to attempt to rob her.")
            self.get_robbed(player)
        elif choice == 'leave':
            print("You decide to leave.")
        else:
            print("Invalid choice. You decide to leave.")

    def give_baby_rock(self, player: Player) -> None:
        """Player finds the crying girl's baby rock."""
        if not self.has_baby_rock:
            for item in player.inventory:
                if item.name == "Baby Rock":
                    player.take_out(item, False)
                    self.has_baby_rock = True
                    player.morale += 3
                    print("Crying Girl: You found my baby!!! Thank you so much!")
                    print("You feel a sense of accomplishment.")
                    break
            if not self.has_baby_rock:  # rock not in inventory
                print("You do not have the rock in your inventory.")
        else:
            print(f"You've already found the baby rock. It's nice to have done a good deed.")
            player.morale += 1


@check_contracts
class MiserableStudent(NPC):
    """A miserable student NPC."""
    has_food: bool = False

    def _rob_attempt(self) -> bool:
        """Robbery attempt for MiserableStudent (always succeeds)."""
        return True

    def prompt(self, player: Player, items: list[Item]) -> None:
        """MiserableStudent talks to the player about finals and asks for food."""
        print(
            f"{self.name} looks stressed and says: I have final exams coming up, and I'm starving...")

        # Check if the player has already bought food for the student
        if self.has_food:
            print("You've already bought food for the student. They look grateful.")
            player.morale += 5
        else:
            print("Options: GIVE FOOD    ROB\tLEAVE")

            choice = input("What to do? ").lower()
            if choice == "give food":
                print("What do you want to give?")
                player.display_inventory()
                inp = input().lower()
                if inp == "candy" or inp == "hot chocolate":
                    for i in player.inventory:
                        if i.name.lower() == inp:
                            player.take_out(i, False)
                            break
                    print("You give the student some candy.")
                    print(f"{self.name}: Ahh sugar... Sugar!! "
                          f"I can feel the glucose (C6H12O6) running through my veins!\
                           Speaking of running, hear's a gift for you. \
                           It seems that you're in a bit of a rush, so this might help!")
                    for i in items:
                        if i.name == "Running Shoes":
                            player.pick_up(i)
                            player.got_running_shoes()
                            break
                    player.morale += 3
                else:
                    print(f"{self.name}: That's not food...")
            elif choice == 'rob':
                print("You decide to attempt to rob them.")
                self.get_robbed(player)
            elif choice == 'leave':
                print("You decide to refuse and leave.")
            else:
                print("Invalid choice. You decide to leave.")


@check_contracts
class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - num: A unique identifier for the location.
        - name: The name of the location.
        - x: The x-coordinate of the location in the game world.
        - y: The y-coordinate of the location in the game world.
        - short_desc: A short description of the location.
        - long_desc: A long description of the location.
        - visited: Indicates whether the player has visited this location.
        - items: A list of items present in the location.
        - npc: The non-player character present in the location (at most one).


    Representation Invariants:
        - self. name >= ' '
        - self. short_desc > ' '
        - self. long_desc > ' '
        - self. visited >=0
    """
    num: int
    name: str
    x: int
    y: int
    short_desc: str
    long_desc: str
    visited: bool
    items: list[Item]
    npc: Optional[NPC]  # there's only gonna be at most one npc at each loc anyway

    def __init__(self, num: int, name: str, pos: tuple, short_desc: str, long_desc: str) -> None:
        """Initialize a new location.
        """

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available actions/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        self.num = num
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.visited = False
        self.items = []
        self.npc = None

    def get_items(self) -> list:
        return self.items

    def get_coords(self) -> tuple:
        return (self.x, self.y)

    def get_npc(self) -> Optional[NPC]:
        return self.npc

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        self.items.remove(item)

    def add_npc(self, enpeecee: NPC) -> None:
        self.npc = enpeecee

    # print actions:
    def print_desc(self) -> None:
        """to be printed when player enters an area.
        """
        print(f"LOCATION: {self.name} - {self.num}\n")
        if self.visited:
            print(self.short_desc)
        else:
            print(self.long_desc)
            self.visited = True

    def print_items(self) -> None:
        if self.items:
            print("There are some items in the vicinity: ")
        for item in self.items:
            print(item.name, "\t")

    def print_look(self) -> None:
        print(self.long_desc)


@check_contracts
class Shop(Location):

    # NOTE!!!!! STATIC VAR VS INSTANCE VAR -- MAKE SURE SHADOWS CORRECTLY!
    def print_wares(self) -> None:
        print("ITEM              PRICE")
        for itm in self.items:
            spaces = 20 - len(itm.name)
            print(f"{itm.name}:{' ' * spaces}${itm.price}")

    def sold(self, item: Item) -> None:  # pair in adventure.py w/ wallet decrease
        print("Thank you for your purchase!")
        self.remove_item(item)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120
    })
