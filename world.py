from typing import Optional, TextIO
from game_data import Location, Item, Shop

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
    map: list

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
    def load_locations(self, location_data: TextIO):
        locs = [None]*23
        current = []    # contains data for one location -- number, name, x, y, short desc, long desc, 
        for line in location_data:  # in numerical order (location 0 = locations[0])
            if 'LOCATION' in line:
                current.append[int(line.split()[1])]
            elif line == '\n':
                locs[current[0]] = Location(current[0], current[1], self.get_location_coords(current[0]), current[2], current[3])
                current = []
            else:
                current.append(str(line))
        return locs
    
    def load_items(self, item_data: TextIO):
        itms = []
        for line in item_data:
            current = line.split(',')
            itms.append(Item(current[4], int(current[2]), int(current[3]), int(current[0]), int(current[1]), current[4]))

    def load_shops(self):
        for item in self.items:
            if (item.x, item.y) == self.get_location_coords(41) or self.get_location_coords(40) or self.get_location_coords(34):
                self.get_location(item.x, item.y).add_ware(item)

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
    
