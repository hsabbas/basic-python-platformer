from src.platformer.blocks.Block import Block, CommonBlocks
from src.platformer.blocks.MovingBlock import MovingBlock


class StageManager:
    def __init__(self):
        self.next_stage = 0
        self.current_stage = self.get_next_stage()

    def reset(self):
        self.__init__()

    def get_stage(self):
        return self.current_stage.get_stage()

    def get_next_stage(self):
        self.next_stage += 1
        stage_map = {
            1: Stage1(),
            2: Stage2(),
            3: Stage3(),
            4: Stage4(),
            5: Stage5()
        }
        self.current_stage = stage_map[self.next_stage]
        return self.current_stage


class Stage:
    def get_stage(self):
        pass


class Stage1(Stage):
    def get_stage(self):
        return [CommonBlocks.get_floor(), CommonBlocks.get_left_wall()]


class Stage2(Stage):
    def __init__(self):
        self.platform1 = Block(200, 100, 200, 200, False)

    def get_stage(self):
        return [self.platform1, CommonBlocks.get_floor(), CommonBlocks.get_left_wall()]


class Stage3(Stage):
    def __init__(self):
        self.platforms = []
        self.platforms.append(Block(40, 70, 100, 230, False))
        self.platforms.append(Block(75, 30, 370, 100, False))
        self.platforms.append(Block(75, 30, 220, 160, False))
        self.platforms.append(Block(50, 200, 550, 100, False))

    def get_stage(self):
        return self.platforms + [CommonBlocks.get_left_wall(), CommonBlocks.get_floor()]


class Stage4(Stage):
    def __init__(self):
        self.floor1 = Block(205, 100, -5, 300, False)
        self.floor2 = Block(205, 100, 400, 300, False)
        self.platform1 = Block(60, 20, 270, 200, False)

    def get_stage(self):
        return  [self.floor1, self.floor2, self.platform1, CommonBlocks.get_left_wall()]


class Stage5(Stage):
    def __init__(self):
        self.enemy1 = MovingBlock(20, 20, 560, 280, True, 20, 580, 280, 280, 10, 0)

    def get_stage(self):
        self.enemy1.move_block()
        return [self.enemy1, CommonBlocks.get_floor(), CommonBlocks.get_left_wall(), CommonBlocks.get_right_wall()]