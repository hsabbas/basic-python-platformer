from src.platformer.blocks.Block import Block


class MovingBlock(Block):
    def __init__(self, size_x, size_y, pos_x, pos_y, is_enemy, leftmost, rightmost, highest, lowest, speed_x, speed_y):
        super().__init__(size_x, size_y, pos_x, pos_y, is_enemy)
        self.leftmost = leftmost
        self.rightmost = rightmost
        self.highest = highest
        self.lowest = lowest
        self.speed_x = speed_x
        self.speed_y = -speed_y

    def update_pos(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        if self.pos_x >= self.rightmost:
            self.pos_x = self.rightmost
            self.speed_x = -self.speed_x

        if self.pos_x <= self.leftmost:
            self.pos_x = self.leftmost
            self.speed_x = -self.speed_x

        if self.pos_y <= self.highest:
            self.pos_y = self.highest
            self.speed_y = -self.speed_y

        if self.pos_y >= self.lowest:
            self.pos_y = self.lowest
            self.speed_y = -self.speed_y
