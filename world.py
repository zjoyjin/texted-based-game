from typing import Optional, TextIO
from game_data import Location, Item, Shop, NPC, RichLady, MiserableStudent, CryingGirl

class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - # TODO add more instance attributes as needed; do NOT remove the map attribute

    Representation Invariants:
        - # TODO
    """
    locations: list[Location]
    items: list[Item]
    map: list[int]
    npcs: list[NPC]

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
        self.npcs = self.load_npcs()
        self.load_shops()


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
        str_map = [line.split() for line in map_data]
        for row in range(len(str_map)):
            for num in range(len(str_map[0])):
                str_map[row][num] = int(str_map[row][num])
        return str_map

    # TODO: Add methods for loading location data and item data (see note above).
    def load_locations(self, location_data: TextIO):
        locs = [None]*47
        current = []    # contains data for one location -- number, name, x, y, short desc, long desc, 
        for line in location_data:  # in numerical order (location 0 = locations[0])
            if 'LOCATION' in line:
                current.append(int(line.split()[1]))
            elif line.strip() == '-':
                if (current[0] != 40 and current[0] != 41 and current[0] != 34):
                    locs[current[0]] = Location(current[0], current[1], self.get_coords_from_num(current[0]), current[2], current[3])
                else:
                    locs[current[0]] = Shop(current[0], current[1], self.get_coords_from_num(current[0]), current[2], current[3])
                current = []
            else:
                current.append(line.strip())
        return locs
    
    def load_items(self, item_data: TextIO):
        itms = []
        for line in item_data:
            current = line.split(',')
            itms.append(Item(current[5].strip(), int(current[2]), int(current[3]), int(current[0]), int(current[1]), current[4]))
        return itms

    def load_shops(self):
        for item in self.items:
            if (item.x, item.y) == self.get_coords_from_num(41) or (item.x, item.y) == self.get_coords_from_num(40) or (item.x, item.y) == self.get_coords_from_num(37):
                self.get_location(item.x, item.y).add_item(item)

    def load_npcs(self):
        return [RichLady("Rich Lady", 10, 8, 9), MiserableStudent("Miserable Student", 0, 5, 7), CryingGirl("Crying Girl", 0, 7, 4)]

    def get_coords_from_num(self, num):
        """
        Precondition:
            - num >= 0
        """
        for y in range(13):
            for x in range(11):
                if self.map[y][x] == num:
                    return (x, y)
        return None

    def get_item_from_name(self, name: str):
        for item in self.items:
            if item.name == name:
                return item
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
    
