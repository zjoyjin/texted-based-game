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


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self, name: str, target_points: int, price: int, x:int, y:int, key_item: str) -> None:
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
        # self.position = start
        # self.target_position = target
        self.x = x
        self.y = y
        self.target_points = target_points
        self.price = price
        if key_item == "False":
            self.key_item = False
        else:
            self.key_item = True


    def update_location(self, x, y):
        """ Update position of item. None if in inventory.
        """
        self.x = x
        self.y = y


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """
    num: int
    name: str
    x: int
    y: int
    short_desc: str
    long_desc: str
    visited: bool = False
    items: list[Item] = []
    
    def __init__(self, num, name, pos, short_desc, long_desc) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
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

        # TODO: Complete this method
        self.num = num
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.short_desc = short_desc
        self.long_desc = long_desc
    
    # TODO: move to adventure.py
    # def update_actions(self, command: Optional[str] = None, key_item: Optional[Item] = None):
    #     """
    #     Return the available actions in this location.
    #     The actions should depend on the items available in the location
    #     and the x,y position of this location on the world map.

    #     if key_item exists, then command must also exist

    #     Preconditions:
    #         - key_item == None or command != None
    #     """
    #     # 2 cases: 1. inspecting yields a new option, 

    #     # TODO: Complete this method, if you'd like or remove/replace it if you're not using it
    #     if command:     #not none
    #         if self.inspected or key_item in self.items:
    #             self.actions.append(command)
    #         elif key_item not in self.items:
    #             self.actions = ["Look", "Move"]
    
    def get_coords(self):
        return (self.x, self.y)
    
    def update_items(self, items = [Item]):
        for itm in items:
            if itm.x == self.x and itm.y == self.y:
                self.items.append(itm)
    
    def get_items(self):
        return(self.items)

    # MOVED TO ADVENTURE.PY
    # def get_directions(self, world) -> list:
    #     """ return the possible movement directions from current location [N,S,E,W]
    #     """
    #     directions = []
    #     # North
    #     if world.get_location(self.x, self.y - 1) is not None:
    #         directions.append(self.N)
    #     #South
    #     if world.get_location(self.x, self.y + 1) is not None:
    #         directions.append(self.S)
    #     #East
    #     if world.get_location(self.x + 1, self.y) is not None:
    #         directions.append(self.E)
    #     #West
    #     if world.get_location(self.x - 1, self.y) is not None:
    #         directions.append(self.W)
    #     return directions
    
    # print actions:
    def print_desc(self) -> None:
        """to be printed when player enters an area.
        """
        print(f"LOCATION: {self.name} - {self.num}\n")
        if self.visited:
            print(self.short_desc)
        else:
            print(self.long_desc)
    
    #TODO: move to adventure.py
    # def print_actions(self) -> None:
    #     for action in self.actions:
    #         print("What to do?")
    #         print(f"[{action}]", end = '\t')
    
    def print_look(self):
        print(self.long_desc)
    
    #TODO: move to adventure.py
    # def print_directions(self) -> None:
    #     for direction in self.get_directions():
    #         print(f"[{direction}]", end = '\t')


class Wallet:
    """Player's wallet in the text adventure game.

    Instance Attributes:
        - money (int): The amount of money in the wallet.
    """

    def __init__(self) -> None:
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
    
    def earn(self, amount: int):
        self.money += amount


def helper_wallet():
    # Example usage
    player_wallet = Wallet()
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
    wallet: Wallet
    steps: int = 0

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
        self.score = 0
        self.location = (x, y)
        self._deposited = set() # for key items

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
    def move(self, dir):        # check for out of bounds in adventure.py
        if dir == "North":
            self.y -= 1
        elif dir == "South":
            self.y += 1
        elif dir == "East":
            self.x += 1
        elif dir == "West":
            self.x -= 1
        
        for itm in self.inventory:
            if itm.name == "Running Shoes":
                self.steps += 1
                break
        else:
            self.steps += 2


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
                print(item + ",", " ")
    
    def print_steps(self):
        print(f"It is {8 + self.score // 60}: {self.score % 60}. Your exam starts at 5:30!")

    def pick_up(self, item: Item):
        """Add an item to the player's inventory.
            item: The item to add to the inventory.
        """
        self.inventory.append(item)
        item.update_location(None, None)
        print(f"You picked up {item}.")

    def take_out(self, item, at_ex: bool):      #at_ex: if we are at exam centre
        """Remove an item from the player's inventory.
        """
        if item in self.inventory and not at_ex and not item.key_item:
            self.inventory.remove(item)
            print(f"You took out {item} from your inventory.")
        elif item in self.inventory and at_ex and item.key_item:
            self.inventory.remove(item)
            self._deposited.add(item)
            self.score += item.score
            print(f"Deposited {item} at the Exam Centre!")
        else:
            print(f"Could not give {item}.")

    def drop(self, item):
        """Drop an item from the player's inventory at a specified location
            item: The item to drop from the inventory.
            location: The location where the item is dropped.
            NOTE: PLEASE DONT LET THEM DROP AT EXAM CENTRE
        """
        if item in self.inventory and not item.key_item:
            self.inventory.remove(item)
            item.update_location(self.x, self.y)
            print(f"You dropped {item.name}.")
        else:
            print(f"Could not drop {item.name}.")
    
    def update_victory(self):
        if self.score > 600 and len(self._deposited) == 3:
            self.victory = True

    def update_moves(self):
        self.moves += 1
    

class NPC:
    """Base class for Non-Playable Characters (NPCs) in the text adventure game.

    Instance Attributes:
        - name (str): The name of the NPC.
        - happiness (int): The happiness level of the NPC.
        - money (int): The amount of money the NPC has.
        - score (int): The score or morale of the NPC.
    """

    def __init__(self, name: str, money: int, score: int) -> None:
        """Initialize a new NPC.
        """
        self.name = name
        self.money = money
        self.score = score

    def talk(self) -> None:
        """NPC talks."""
        print(f"{self.name} says: Hello! How are you today?")

    def rob(self, player) -> None:
        """Player attempts to rob the NPC."""
        print(f"You attempt to rob {self.name}.")
        if self._rob_attempt():
            print(f"You successfully rob {self.name}!")
            player.wallet.earn(self.money)
            self.money = 0
            self.score -= 5
        else:
            print(f"Your robbery attempt on {self.name} fails!")
            self.score -= 2

    def leave(self) -> None:
        """NPC leaves."""
        print(f"{self.name} says goodbye and leaves.")

    def _rob_attempt(self) -> bool:
        """Simulate a robbery attempt."""
        # Override this method in subclasses to customize robbery behavior.
        return False

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
            player.score += 2
        elif choice == '2':
            print("You insult her back, but it only escalates the situation.")
            player.score -= 3
        elif choice == '3':
            print("You decide to attempt to rob her in response to the harassment.")
            self._rob_attempt(player)
        elif choice == '4':
            print("You decide to leave to avoid further confrontation.")
        else:
            print("Invalid choice. You decide to leave.")

class CryingGirl(NPC):
    """A crying girl NPC."""

    # def __init__(self, name: str, happiness: int, money: int, score: int, has_baby_rock: bool = False) -> None:
    #     """Initialize a new CryingGirl.
    #     """
    #     self.has_baby_rock = has_baby_rock
    has_baby_rock = False

    def _rob_attempt(self) -> bool:
        """Robbery attempt for CryingGirl (always fails)."""
        return False

    def request_baby_rock(self, player) -> None:
        """CryingGirl talks to the player and requests them to find a baby rock."""
        print(f"{self.name}: *Sob* Oh dear, oh dear... Could you please find a baby rock for me? It means a lot. *Sob*")
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
            player.pick_up("Baby Rock")
            self.has_baby_rock = True
            player.score += 3
            print("You feel a sense of accomplishment and gain happiness!")
        else:
            print(f"You've already found the baby rock near {self.name}.")
            player.score += 1
            print("You feel a bit better about yourself.")


class MiserableStudent(NPC):
    """A miserable student NPC."""

    # def __init__(self, name: str, happiness: int, money: int, score: int, has_food: bool = False) -> None:
    #     """Initialize a new MiserableStudent.
    #     """
    #     self.has_food = has_food
    
    has_food = False
    
    def _rob_attempt(self) -> bool:
        """Robbery attempt for MiserableStudent (always succeeds)."""
        return True

    def ask_for_food(self, player, items: [Item]) -> None:
        """MiserableStudent talks to the player about finals and asks for food."""
        print(
            f"{self.name} looks stressed and says: I have final exams coming up, and I'm starving...")

        # Check if the player has already bought food for the student
        if self.has_food:
            print("You've already bought food for the student. They look grateful.")
            player.score += 2
        else:
            print("Options:")
            print("1. Give food")
            print("2. Refuse and leave.")

            choice = input("Enter your choice (1 or 2): ")
            if choice == '1':
                print("What do you want to give?")
                player.display_inventory()
                inp = input().lower()
                if inp == "candy" or inp == "hot chocolate":
                    for i in items:
                        if i.name.lower() == inp:
                            self.take_out(i)
                            break
                    print("You give the student some candy.")
                    print(f"{self.name}: Ahh sugar... Sugar!! I can feel the glucose (C6H12O6) running through my veins!\
                           Speaking of running, hear's a gift for you. It seems that you're in a bit of a rush, so this might help!")
                    for i in items:
                        if i.name == "Running Shoes":
                            self.pick_up(i)
                            break
                else:
                    print(f"{self.name}: That's not food...")
            elif choice == '2':
                print("You decide to refuse and leave.")
            else:
                print("Invalid choice. You decide to leave.")


class Shop(Location):
    num: int
    name: str
    x: int
    y: int
    short_desc: str
    long_desc: str
    visited: bool = False
    wares: list[Item]

    def add_ware(self, itm: Item):
        self.append(itm)

    def print_wares(self):
        print("ITEM \tPRICE")
        for itm in self.wares:
            print(f"{itm.name}:\t${itm.price}")

    def sold(self, item):      # pair in adventure.py w/ wallet decrease
        print("Thank you for your purchase!")
        self.wares.pop(item)