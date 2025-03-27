import copy


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(
        self,
        x=0,
        y=0,
        char="?",
        color=(255, 255, 255),
        name="<Unnamed>",
        blocks_movement=False,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

    def spawn(self, gamemap, x, y):
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
