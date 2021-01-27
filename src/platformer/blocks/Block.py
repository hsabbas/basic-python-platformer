class Block:
    def __init__(self, size_x, size_y, pos_x, pos_y, is_enemy):
        self.size_x = size_x
        self.size_y = size_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.enemy = is_enemy


class CommonBlocks:
    @staticmethod
    def get_floor():
        return Block(610, 100, -5, 300, False)

    @staticmethod
    def get_left_wall():
        return Block(1, 400, -2, 0, False)

    @staticmethod
    def get_right_wall():
        return Block(1, 400, 601, 0, False)