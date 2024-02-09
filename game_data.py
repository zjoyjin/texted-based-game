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
        - name (str): name of item
        - x (int): x coordinate of item (in game map), or None if item in player inventory.
        - y (int): y coordinate of item (in game map), or None if item in player inventory.
        - price (int): item price (notably for purchaseable items in shops)
        - key_item (bool): if this item is a key item, i.e. T Card, Lucky Pen, or Cheat Sheet

    Representation Invariants:
        - self.name != ''
        - self.x is None or (self.x >=0 and self.x <= 10)
        - self.y is None or (self.y >= 0 and self.y <= 12)
        - self.price >= 0
    """
    name: str
    x: Optional[int]
    y: Optional[int]
    price: int
    key_item: bool

    def __init__(self, name: str, price: int, location: tuple, key_item: str) -> None:
        """Initialize a new item.
        """
        self.name = name
        self.x = location[0]
        self.y = location[1]
        self.price = price
        if key_item == "False":
            self.key_item = False
        else:
            self.key_item = True

    def update_location(self, x: Optional[int], y: Optional[int]) -> None:
        """ Update position of item. None if in inventory. x, y == 0, 0 if permanently removed from inventory.
        Preconditions:
            - x is None or (x >=0 and x <= 10)
            - y is None or (y >= 0 and y <= 12)
        """
        self.x = x
        self.y = y


@check_contracts
class Wallet:
    """Player's wallet in the text adventure game.

    Instance Attributes:
        - money (int): The amount of money in the wallet.

    Representation Invariants:
        - self.money >= 0
    """
    money: int

    def __init__(self) -> None:
        """Initialize the wallet with an initial amount of money.
        """
        self.money = 25

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
        """ Gain money (by robbing).
        """
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
        - morale: the player's morale (score)
        - step: the total number of steps the player has taken, represented in-game as time
        - _has_running_shoes: if player have running shoes or not

    Representation Invariants:
        - self.wallet.money >= 0
        - self.steps >=0
        - self.x >=0 and self.x <= 10
        - self.y >= 0 and self.y <= 12
        - len(self._deposited) <= 3

    """
    x: int
    y: int
    inventory: list[Item]
    wallet: Wallet
    morale: int
    steps: int
    _deposited: set[Item]  # for key items
    _has_running_shoes: bool

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        self.x = x
        self.y = y
        self.inventory = []
        self.wallet = Wallet()
        self.morale = 0
        self.steps = 0
        self._deposited = set()
        self._has_running_shoes = False

    def move(self, direction: str) -> None:
        """ Update player coordinates according to movement direction.
        """
        if direction == "NORTH":
            self.y -= 1
        elif direction == "SOUTH":
            self.y += 1
        elif direction == "EAST":
            self.x += 1
        elif direction == "WEST":
            self.x -= 1

    def print_morale(self) -> None:
        """ Prints player morale (score).
        """
        print(f"Your morale is {self.morale}")

    def display_inventory(self) -> None:
        """Display the items in the player's inventory.
        """
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for item in self.inventory:
                print(item.name, ", ")
            print("\n")

    def print_steps(self) -> None:
        """Print step count to player, represented as time elapsed in-game.
        """
        print(f"It is {8 + self.steps // 60}: {self.steps % 60}. Your exam starts at 5:30!")

    def pick_up(self, item: Item) -> None:
        """Add an item to the player's inventory.
            item: The item to add to the inventory.
        """
        self.inventory.append(item)
        item.update_location(None, None)
        print(f"You picked up {item.name}.")

    def take_out(self, item: Item, at_ex: bool) -> None:
        """Permanently remove an item from the player's inventory.
        Updates item coords to (0,0) (inaccessible location to player)
        at_ex: whether or not the player is at the exam centre location
            If depositing a key item at exam centre, also updates self._deposited and morale.

        Precondition:
            - item in self.inventory
        """
        # giving to miserable student:
        if not at_ex and not item.key_item:
            self.inventory.remove(item)
            item.update_location(0, 0)
            print(f"You took out {item.name} from your inventory.")
        # depositing at exam centre:
        elif at_ex and item.key_item:
            self.inventory.remove(item)
            item.update_location(0, 0)
            self._deposited.add(item)
            self.morale += 5
            print(f"Deposited {item.name} at the Exam Centre!")
        else:
            print(f"Could not take out {item.name}.")

    def drop(self, item: Item) -> None:
        """Drop an item from the player's inventory at a specified location.
            Cannot drop at exam centre or shops.
            item: The item to drop from the inventory.
            location: The location where the item is dropped.
        Precondition:
            - item in self.inventory
        """
        self.inventory.remove(item)
        item.update_location(self.x, self.y)
        if item.name == "Running Shoes":
            self._has_running_shoes = False
        print(f"You dropped {item.name}.")

    def display_balance(self) -> None:
        """Display the current balance in the wallet.
        """
        print(f"Wallet Balance: ${self.wallet.money}", "\t")

    def update_steps(self) -> None:
        """ Update player step count (represented in-game as time)
        Steps taken decreases w/ the acquisition of running shoes item.
        """
        if self._has_running_shoes:
            self.steps += 1
        else:
            self.steps += 2

    def got_running_shoes(self) -> None:
        """ Called if player obtains running shoes (from Miserable Student npc)
        """
        self._has_running_shoes = True

    def check_victory(self) -> bool:
        """ Check if player has deposited all 3 key items.
        """
        if len(self._deposited) == 3:
            return True
        return False


@check_contracts
class NPC:
    """Base class for Non-Playable Characters (NPCs) in the text adventure game.

    Instance Attributes:
        - name (str): The name of the NPC.
        - x (int): the x coord of the NPC (in map)
        - y (int): the y coord of the NPC (in map)

     Representation Invariants:
        - self.name != ''
        - self.x >=0 and self.x <= 10
        - self.y >= 0 and self.y <= 12
    """
    name: str
    x: int
    y: int

    def __init__(self, name: str, x: int, y: int) -> None:
        """Initialize a new NPC.
        """
        self.name = name
        self.x = x
        self.y = y

    def get_robbed(self, player: Player) -> None:
        """Player attempts to rob the NPC."""
        print(f"You attempt to rob {self.name}.")
        if self._rob_attempt():
            print(f"You successfully rob {self.name}!")
            player.wallet.earn(50)
            player.morale -= 4
        else:
            print(f"Your robbery attempt on {self.name} fails!")
            player.morale -= 5

    def _rob_attempt(self) -> bool:
        """Simulate a robbery attempt."""
        # Override this method in subclasses to customize robbery behavior.
        return False


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
        print("Options: GIVE BABY ROCK    ROB    LEAVE")

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
        """Player finds the crying girl's baby rock.
        First checks if the girl already has the rock, then checks if rock
        is in player inventory.
        """
        if not self.has_baby_rock:
            for item in player.inventory:
                if item.name == "Baby Rock":
                    player.take_out(item, False)
                    self.has_baby_rock = True
                    player.morale += 3
                    print(f"{self.name}: You found my baby!!! Thank you so much!")
                    print("You feel a sense of accomplishment.")
                    break
            if not self.has_baby_rock:
                print("You do not have the rock in your inventory.")
        else:
            print("You've already found the baby rock. It's nice to have done a good deed.")
            player.morale += 1


@check_contracts
class MiserableStudent(NPC):
    """A miserable student NPC."""
    has_food: bool = False

    def _rob_attempt(self) -> bool:
        """Robbery attempt for MiserableStudent (always succeeds)."""
        return True

    def quest_success(self, inp: str, player: Player, items: list[Item]) -> None:
        """Called when the player successfully gives this NPC food.
        inp: the name of the food item the user is giving (user input)
        player: the player
        items: list of all the items in the world (to get the running shoes item by name)
        """
        for i in player.inventory:
            if i.name.lower() == inp:
                player.take_out(i, False)
                break
        print("You give the student some candy.")
        print(f"{self.name}: Ahh sugar... Sugar!! \
              I can feel the glucose (C6H12O6) running through my veins!\
              Speaking of running, hear's a gift for you. \
              It seems that you're in a bit of a rush, so this might help!")
        for i in items:
            if i.name == "Running Shoes":
                player.pick_up(i)
                player.got_running_shoes()
                break
        player.morale += 3

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
                if inp in {"candy", "hot chocolate"}:
                    self.quest_success(inp, player, items)
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
        - self.name != ''
        - self.short_desc != ''
        - self.long_desc != ''
        - self.x >=0 and self.x <= 10
        - self.y >= 0 and self.y <= 12
        - self.num >= 0 and self.num <= 46
    """
    num: int
    name: str
    x: int
    y: int
    short_desc: str
    long_desc: str
    visited: bool
    items: list[Item]
    npc: Optional[NPC]

    def __init__(self, num: int, name: str, pos: tuple, short_desc: str, long_desc: str) -> None:
        """Initialize a new location.
        """
        self.num = num
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.visited = False
        self.items = []
        self.npc = None

    def get_items(self) -> list[Item]:
        """ Get list of items at location.
        """
        return self.items

    # def get_coords(self) -> tuple[int]:
    #     """ Get coordinates"""
    #     return (self.x, self.y)


    def get_npc(self) -> Optional[NPC]:
        """Get NPC at location, if any
        """
        return self.npc

    def add_item(self, item: Item) -> None:
        """Add item to list of items at location.
        """
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        """Remove item from list of items at location.
        Preconditions:
            - item in self.items
        """
        self.items.remove(item)

    def add_npc(self, enpeecee: NPC) -> None:
        """Add npc to location. Only called once during location setup (world.py)
        Preconditions:
            - self.npc is None
        """
        self.npc = enpeecee

    def print_desc(self) -> None:
        """Description to be printed when player enters location.
        """
        print(f"LOCATION: {self.name} - {self.num}\n")
        if self.visited:
            print(self.short_desc)
        else:
            print(self.long_desc)
            self.visited = True

    def print_items(self) -> None:
        """ Print items at location. To be printed upon player entry to location.
        """
        if self.items:
            print("There are some items in the vicinity: ")
        for item in self.items:
            print(item.name, "\t")

    def print_look(self) -> None:
        """ Prints long description.
        """
        print(self.long_desc)


@check_contracts
class Shop(Location):
    """
    A shop in our text adventure game world from which items can be purhcased.
    Initialized the same as a Location.
    """

    def print_wares(self) -> None:
        """ Prints list of items + price
        """
        print("ITEM              PRICE")
        for itm in self.items:
            spaces = 20 - len(itm.name)
            print(f"{itm.name}:{' ' * spaces}${itm.price}")

    def sold(self, item: Item) -> None:
        """ removes sold item from list of items.
        Preconditions:
            - item in self.items
        """
        print("Thank you for your purchase!")
        self.remove_item(item)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120
    })
