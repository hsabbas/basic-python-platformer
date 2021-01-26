from src.platformer.entities.Entity import Entity


right_wall = Entity(1, 400, 601, 0, False)


class StageManager:
    def __init__(self):
        self.next_stage = 0
        self.current_stage = self.get_next_stage()

    def get_stage(self):
        return self.current_stage.get_stage()

    def get_next_stage(self):
        self.next_stage += 1
        stage_map = {
            1: Stage1(),
            2: Stage2()
        }
        self.current_stage = stage_map[self.next_stage]
        return self.current_stage

class Stage:
    def get_stage(self):
        pass

class Stage1(Stage):
    def __init__(self):
        self.platform1 = Entity(200, 100, 300, 200, False)

    def get_stage(self):
        return [self.platform1]


class Stage2(Stage):
    def __init__(self):
        self.platform1 = Entity(40, 70, 60, 230, False)
        self.platform2 = Entity(40, 160, 140, 140, False)

    def get_stage(self):
        return [self.platform1, self.platform2, right_wall]