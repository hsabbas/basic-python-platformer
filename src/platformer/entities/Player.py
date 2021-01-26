from src.platformer.entities.Entity import Entity


class Player(Entity):
    def __init__(self, size_x, size_y, pos_x, pos_y):
        super().__init__(size_x, size_y, pos_x, pos_y, False)
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

    def update_pos(self, entities):
        self.pos_x += self.change_x

        self.change_y += self.gravity
        self.pos_y += self.change_y

        for entity in entities:
            self.check_collides_with(entity)

        if self.change_y != 0:
            self.grounded = False

    def above_or_below(self, entity):
        return entity.pos_x - self.size_x < self.pos_x < entity.pos_x + entity.size_x

    def collides_right_with(self, entity):
        return entity.pos_x <= self.pos_x + self.size_x <= entity.pos_x + self.movement_speed \
           and self.same_level_as(entity)

    def collides_left_with(self, entity):
        return entity.pos_x + entity.size_x - self.movement_speed <= self.pos_x <= entity.pos_x + entity.size_x \
            and self.same_level_as(entity)

    def same_level_as(self, entity):
        return entity.pos_y - self.size_y < self.pos_y < entity.pos_y + entity.size_y

    def collides_below_with(self, entity):
        return entity.pos_y - self.size_y <= self.pos_y <= entity.pos_y + self.change_y\
           and self.above_or_below(entity) and self.change_y >= 0

    def collides_above_with(self, entity):
        return self.change_y < 0 and \
            entity.pos_y + entity.size_y + self.change_y <= self.pos_y < entity.pos_y + entity.size_y and \
            self.above_or_below(entity)

    def check_collides_with(self, entity):
        if self.change_x > 0:
            if self.collides_right_with(entity):
                self.pos_x = entity.pos_x - self.size_x - 1

        if self.change_x < 0:
            if self.collides_left_with(entity):
                self.pos_x = entity.pos_x + entity.size_x + 1

        if self.collides_below_with(entity):
            self.pos_y = entity.pos_y - self.size_y - 1
            self.land()

        if self.collides_above_with(entity):
            self.pos_y = entity.pos_y + entity.size_y
            self.stop_jump()

    def go_to_start(self):
        self.pos_x = 0