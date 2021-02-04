import pygame

from src.platformer.blocks.Player import Player
from src.platformer.stages.Stages import StageManager


class Game:
    pygame.init()
    display_width = 600
    display_height = 400
    display = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    player_size = 20
    player = Player(player_size, player_size, 20, 280)

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    stage_manager = StageManager()
    current_stage_number = 1
    stage_manager.load_stage(current_stage_number)
    current_stage_blocks = stage_manager.get_stage()

    def draw_stage(self):
        self.display.fill(self.white)
        for block in self.current_stage_blocks:
            if block.enemy:
                self.draw_enemy(block)
            else:
                self.draw_block(block)

    def draw_enemy(self, block):
        pygame.draw.rect(self.display, self.black, (block.pos_x - 1, block.pos_y - 1, block.size_x + 2, block.size_y + 2))
        pygame.draw.rect(self.display, self.red, (block.pos_x, block.pos_y, block.size_x, block.size_y))

    def draw_block(self, block):
        pygame.draw.rect(self.display, self.black, (block.pos_x - 1, block.pos_y - 1, block.size_x + 2, block.size_y + 2))
        pygame.draw.rect(self.display, self.white, (block.pos_x, block.pos_y, block.size_x, block.size_y))

    def draw_game(self):
        self.draw_stage()
        self.draw_block(self.player)

    def check_next_stage(self):
        if self.player.pos_x >= self.display_width:
            self.load_next_stage()

    def load_next_stage(self):
        self.player.go_to_start()
        self.current_stage_number += 1
        self.stage_manager.load_stage(self.current_stage_number)
        self.current_stage_blocks = self.stage_manager.get_stage()

    def check_death(self):
        if self.player.dead:
            self.current_stage_number = 1
            self.stage_manager.load_stage(self.current_stage_number)
            self.current_stage_blocks = self.stage_manager.get_stage()
            self.player.go_to_start()

    def main(self):
        self.draw_game()
        pygame.display.update()

        game_close = False
        while not game_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    if event.key == pygame.K_x:
                        self.player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_x:
                        self.player.stop_jump()
                    if event.key == pygame.K_LEFT and self.player.change_x < 0 \
                            or event.key == pygame.K_RIGHT and self.player.change_x > 0:
                        self.player.stop_x()

            self.current_stage_blocks = self.stage_manager.get_stage()
            self.player.update_pos(self.current_stage_blocks)
            self.check_next_stage()

            self.draw_game()
            pygame.display.update()
            self.check_death()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.main()
    pygame.quit()
    quit()
