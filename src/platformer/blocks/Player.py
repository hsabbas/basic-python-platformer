from blocks.Block import Block


class Player(Block):
    def __init__(self, size_x, size_y, pos_x, pos_y):
        super().__init__(size_x, size_y, pos_x, pos_y, False)
        self.dead = False
        self.grounded = True
        self.gravity = 1
        self.jump_force = -18
        self.movement_speed = 5
        self.change_x = 0
        self.change_y = 0

    def move_left(self):
        self.change_x = -self.movement_speed

    def move_right(self):
        self.change_x = self.movement_speed

    def jump(self):
        if self.grounded:
            self.change_y = self.jump_force
            self.grounded = False

    def stop_x(self):
        self.change_x = 0

    def stop_jump(self):
        if self.change_y < 0:
            self.change_y = 0

    def land(self):
        self.grounded = True
        self.change_y = 0

    def update_pos(self, blocks):
        self.pos_x += self.change_x

        self.change_y += self.gravity
        self.pos_y += self.change_y

        for block in blocks:
            self.check_collides_with(block)

        if self.change_y != 0:
            self.grounded = False

        if self.pos_y >= 400:
            self.dead = True
            self.pos_y = 280

    def above_or_below(self, block):
        return block.pos_x - self.size_x < self.pos_x < block.pos_x + block.size_x

    def collides_right_with(self, block):
        return block.pos_x <= self.pos_x + self.size_x <= block.pos_x + self.movement_speed \
               and self.same_level_as(block)

    def collides_left_with(self, block):
        return block.pos_x + block.size_x - self.movement_speed <= self.pos_x <= block.pos_x + block.size_x \
               and self.same_level_as(block)

    def same_level_as(self, block):
        return block.pos_y - self.size_y < self.pos_y < block.pos_y + block.size_y

    def collides_below_with(self, block):
        return block.pos_y - self.size_y <= self.pos_y <= block.pos_y + self.change_y \
               and self.above_or_below(block) and self.change_y >= 0

    def collides_above_with(self, block):
        return self.change_y < 0 and \
               block.pos_y + block.size_y + self.change_y <= self.pos_y < block.pos_y + block.size_y and \
               self.above_or_below(block)

    def check_collides_with(self, block):
        collision = False
        if self.change_x > 0:
            if self.collides_right_with(block):
                self.pos_x = block.pos_x - self.size_x - 1
                collision = True

        if self.change_x < 0:
            if self.collides_left_with(block):
                self.pos_x = block.pos_x + block.size_x + 1
                collision = True

        if self.collides_below_with(block):
            self.pos_y = block.pos_y - self.size_y - 1
            self.land()
            collision = True

        if self.collides_above_with(block):
            self.pos_y = block.pos_y + block.size_y
            self.stop_jump()
            collision = True

        if collision and block.enemy:
            self.dead = True

    def go_to_start(self):
        self.pos_x = 5
        self.dead = False
