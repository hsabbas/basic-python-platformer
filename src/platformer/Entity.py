class Entity:
    def __init__(self, size_x, size_y, pos_x, pos_y, is_enemy):
        self.size_x = size_x
        self.size_y = size_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.enemy = is_enemy


class Floor(Entity):
    def __init__(self):
        super().__init__(600, 100, 0, 300, False)