from blocks.Block import Block, CommonBlocks
from blocks.MovingBlock import MovingBlock


class StageManager:
    def __init__(self):
        self.current_stage = Stage1()

    def reset(self):
        self.__init__()

    def get_stage(self):
        return self.current_stage.get_stage()

    def load_stage(self, stage_number):
        stage_map = {
            1: Stage1(),
            2: Stage2(),
            3: Stage3(),
            4: Stage4(),
            5: Stage5(),
            6: Stage6(),
            7: Stage7(),
            8: Stage8(),
            9: Stage9(),
            10: Stage10(),
            11: Stage11(),
            12: Stage12(),
            13: Stage13(),
            14: Stage14(),
            15: Stage15(),
            16: Stage16()
        }
        self.current_stage = stage_map[stage_number]


class Stage:
    def get_stage(self):
        pass


class Stage1(Stage):
    def get_stage(self):
        return [CommonBlocks.get_floor(), CommonBlocks.get_left_wall()]


class Stage2(Stage):
    def __init__(self):
        self.platform1 = Block(200, 99, 200, 200, False)

    def get_stage(self):
        return [CommonBlocks.get_floor(), self.platform1, CommonBlocks.get_left_wall()]


class Stage3(Stage):
    def __init__(self):
        self.platforms = []
        self.platforms.append(Block(75, 30, 160, 200, False))
        self.platforms.append(Block(75, 30, 310, 130, False))
        self.platforms.append(Block(120, 199, 485, 100, False))

    def get_stage(self):
        return [CommonBlocks.get_left_wall(), CommonBlocks.get_floor()] + self.platforms


class Stage4(Stage):
    def __init__(self):
        self.floor1 = Block(205, 100, -5, 300, False)
        self.floor2 = Block(205, 100, 400, 300, False)
        self.platform1 = Block(60, 20, 270, 200, False)

    def get_stage(self):
        return [self.floor1, self.floor2, self.platform1, CommonBlocks.get_left_wall()]


class Stage5(Stage):
    def __init__(self):
        self.floor1 = Block(135, 100, -5, 300, False)
        self.floor2 = Block(135, 100, 470, 300, False)
        self.platform1 = Block(60, 20, 193, 200, False)
        self.platform2 = Block(60, 20, 359, 200, False)

    def get_stage(self):
        return [self.floor1, self.floor2, self.platform1, self.platform2, CommonBlocks.get_left_wall()]


class Stage6(Stage):
    def __init__(self):
        self.floor1 = Block(150, 100, -5, 300, False)
        self.platforms = []
        self.platforms.append(Block(75, 30, 220, 200, False))
        self.platforms.append(Block(75, 30, 370, 130, False))
        self.platforms.append(Block(50, 300, 550, 100, False))

    def get_stage(self):
        return [self.floor1, CommonBlocks.get_left_wall()] + self.platforms


class Stage7(Stage):
    def __init__(self):
        self.enemy1 = Block(40, 40, 280, 259, True)

    def get_stage(self):
        return [CommonBlocks.get_left_wall(), CommonBlocks.get_floor(), self.enemy1]


class Stage8(Stage):
    def __init__(self):
        self.enemy1 = MovingBlock(20, 20, 560, 280, True, 0, 580, 280, 280, 5, 0)

    def get_stage(self):
        self.enemy1.update_pos()
        return [self.enemy1, CommonBlocks.get_floor(), CommonBlocks.get_left_wall()]


class Stage9(Stage):
    def __init__(self):
        self.floor1 = Block(255, 100, -5, 300, False)
        self.floor2 = Block(255, 100, 350, 300, False)
        self.enemy1 = MovingBlock(20, 20, 290, 0, True, 290, 290, 40, 300, 0, 5)

    def get_stage(self):
        self.enemy1.update_pos()
        return [self.floor1, self.floor2, self.enemy1, CommonBlocks.get_left_wall()]


class Stage10(Stage):
    def __init__(self):
        self.floor = []
        self.floor.append(Block(255, 100, -5, 300, False))
        self.floor.append(Block(255, 100, 350, 300, False))
        self.deadly_floor1 = Block(100, 100, 250, 300, True)

    def get_stage(self):
        return self.floor + [self.deadly_floor1, CommonBlocks.get_left_wall()]


class Stage11(Stage):
    def __init__(self):
        self.enemy1 = MovingBlock(20, 20, 560, 280, True, 0, 580, 280, 280, 10, 0)

    def get_stage(self):
        self.enemy1.update_pos()
        return [self.enemy1, CommonBlocks.get_floor(), CommonBlocks.get_left_wall()]


class Stage12(Stage):
    def __init__(self):
        self.platforms = []
        self.platforms.append(Block(175, 100, -5, 300, False))
        self.platforms.append(Block(60, 20, 270, 240, False))
        self.platforms.append(Block(60, 20, 150, 90, False))
        self.platforms.append(Block(155, 20, 450, 380, False))
        self.platforms.append(Block(280, 20, 330, -21, False))
        self.platforms.append(Block(100, 300, 500, 0, False))

    def get_stage(self):
        return [CommonBlocks.get_left_wall()] + self.platforms


class Stage13(Stage):
    def __init__(self):
        self.platforms = []
        self.platforms.append(Block(599, 20, 1, 100, False))
        self.platforms.append(Block(610, 20, -5, 380, False))
        self.platforms.append(Block(55, 105, 550, 300, False))
        self.enemy1 = MovingBlock(20, 20, 140, 360, True, 0, 530, 360, 360, 5, 0)
        self.enemy2 = MovingBlock(20, 20, 335, 360, True, 0, 530, 360, 360, 5, 0)
        self.enemy3 = MovingBlock(20, 20, 530, 360, True, 0, 530, 360, 360, 5, 0)

    def get_stage(self):
        self.enemy1.update_pos()
        self.enemy2.update_pos()
        self.enemy3.update_pos()
        return [self.enemy1, self.enemy2, self.enemy3, CommonBlocks.get_left_wall()] + self.platforms


class Stage14(Stage):
    def __init__(self):
        self.platform1 = Block(600, 20, 0, 100, False)
        self.enemy1 = MovingBlock(20, 20, 180, 79, True, 0, 580, 79, 79, 4, 0)
        self.enemy2 = MovingBlock(20, 20, 380, 79, True, 0, 580, 79, 79, 4, 0)
        self.enemy3 = MovingBlock(20, 20, 580, 79, True, 0, 580, 79, 79, 4, 0)

    def get_stage(self):
        self.enemy1.update_pos()
        self.enemy2.update_pos()
        self.enemy3.update_pos()
        return [self.platform1, self.enemy1, self.enemy2, self.enemy3, CommonBlocks.get_left_wall(), CommonBlocks.get_floor()]


class Stage15(Stage):
    def __init__(self):
        self.platforms = []
        self.platforms.append(Block(125, 20, -5, 100, False))
        self.platforms.append(Block(125, 100, -5, 300, False))
        self.platforms.append(Block(125, 100, 480, 300, False))
        self.platforms.append(Block(200, 20, 200, 200, False))
        self.enemy1 = MovingBlock(20, 20, 200, 179, True, 200, 380, 179, 179, 5, 0)

    def get_stage(self):
        self.enemy1.update_pos()
        return [self.enemy1, CommonBlocks.get_left_wall()] + self.platforms


class Stage16(Stage):
    def __init__(self):
        self.enemies = []
        self.enemies.append(MovingBlock(20, 20, 100, 320, True, 100, 100, 40, 320, 0, 5))
        self.enemies.append(MovingBlock(20, 20, 300, 40, True, 300, 300, 40, 320, 0, 5))
        self.enemies.append(MovingBlock(20, 20, 500, 320, True, 500, 500, 40, 320, 0, 5))

    def get_stage(self):
        self.enemies[0].update_pos()
        self.enemies[1].update_pos()
        self.enemies[2].update_pos()
        return self.enemies + [CommonBlocks.get_left_wall(), CommonBlocks.get_floor(), CommonBlocks.get_right_wall()]
