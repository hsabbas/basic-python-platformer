from src.platformer.blocks.Block import Block


class MovingBlock(Block):
    def __init__(self, size_x, size_y, pos_x, pos_y, is_enemy, left_end, right_end, top_end, bottom_end, speed_x, speed_y):
        super().__init__(size_x, size_y, pos_x, pos_y, is_enemy)
        self.left_end = left_end
        self.right_end = right_end
        self.top_end = top_end
        self.bottom_end = bottom_end
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move_block(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        if self.pos_x >= self.right_end:
            self.pos_x = self.right_end
            self.speed_x = -self.speed_x

        if self.pos_x <= self.left_end:
            self.pos_x = self.left_end
            self.speed_x = -self.speed_x


        if self.pos_y >= self.top_end:
            self.pos_y = self.top_end
            self.speed_y = -self.speed_y

        if self.pos_y <= self.bottom_end:
            self.pos_y = self.bottom_end
            self.speed_y = -self.speed_y