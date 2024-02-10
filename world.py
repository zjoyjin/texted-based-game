"""
This Python module contains the World class in which all other classes are initialized and the world map.
Also contains additional helper functions, such as getting a location number from xy coords.
"""


from typing import Optional, TextIO
from game_data import Location, Item, Shop, NPC, RichLady, MiserableStudent, CryingGirl


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - items: list of all Items in the world
        - locations: list of all Locations in the world
        - npcs: list of all NPCs in the world

    Representation Invariants:
        - len(self.locations) == 47
        - len(self.items) == 10
        - len(self.npcs) == 3
        - len(self.map) == 12 and len(self.map[0]) == 11
    """
    locations: list[Location]
    items: list[Item]
    map: list[int]
    npcs: list[NPC]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - map_data: name of text file containing map data
        - location_data: name of text file containing location data
        - items_data: name of text file containing item data
        """
        self.map = self.load_map(map_data)
        self.locations = self.load_locations(location_data)
        self.items = self.load_items(items_data)
        self.npcs = self.load_npcs()
        self.init_items_and_npc_to_loc()

    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.

        Preconditions:
            - map_data != ''
        """
        str_map = [line.split() for line in map_data]
        return [[int(num) for num in row] for row in str_map]

    def load_locations(self, location_data: TextIO) -> list[Location]:
        """ Initializes Location objects from text file and returns list containing them.
        The returned list is ordered by number, so index 0 -> location with num = 0, etc.
        Shops are initialized too.

        Preconditions:
            - location_data != ''
        """
        locs = [None] * 47
        current = []
        for line in location_data:
            if 'LOCATION' in line:
                current.append(int(line.split()[1]))
            elif line.strip() == '-':
                if (current[0] != 40 and current[0] != 41 and current[0] != 37):
                    locs[current[0]] = Location(current[0], current[1],
                                                self.get_coords_from_num(current[0]), current[2], current[3])
                else:
                    locs[current[0]] = Shop(current[0], current[1],
                                            self.get_coords_from_num(current[0]), current[2], current[3])
                current = []
            else:
                current.append(line.strip())
        return locs

    def load_items(self, item_data: TextIO) -> list[Item]:
        """ Initializes Item objects from text file and returns list containing them.

        Preconditions:
            - item_data != ''
        """
        itms = []
        for line in item_data:
            current = line.split(',')
            itms.append(Item(current[4].strip(), int(current[2]), (int(current[0]), int(current[1])), current[3]))
        return itms

    def load_npcs(self) -> list[NPC]:
        """ Initializes NPC objects and returns list containing them.
        """
        return [RichLady("Rich Lady", 8, 9), MiserableStudent("Miserable Student", 5, 7),
                CryingGirl("Crying Girl", 7, 4)]

    def init_items_and_npc_to_loc(self) -> None:
        """
        Adds all Item and NPC objects to their respective locations
        (Updates corresponding Location object's `items` and `npc` vars)
        """
        for item in self.items:
            for location in self.locations:
                if (item.x, item.y) == (location.x, location.y):
                    location.add_item(item)
        for npc in self.npcs:
            for location in self.locations:
                if (npc.x, npc.y) == (location.x, location.y):
                    location.add_npc(npc)

    def get_coords_from_num(self, num: int) -> Optional[tuple[int]]:
        """
        Get the xy position of the location with number `num`.
        Returns None if location with number `num` is not found for whatever reason.
        Preconditions:
            - num >= 0 and num <= 46
        """
        for y in range(13):
            for x in range(11):
                if self.map[y][x] == num:
                    return (x, y)
        return None

    def get_item_from_name(self, name: str) -> Optional[Item]:
        """ Returns Item object with inputted name.
        """
        for item in self.items:
            if item.name == name:
                return item
        return None

    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        num = self.map[y][x]
        if num == -1:
            return None
        return self.locations[num]
