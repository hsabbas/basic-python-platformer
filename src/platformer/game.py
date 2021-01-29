import pygame

from src.platformer.blocks.Player import Player
from src.platformer.stages.Stages import StageManager

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
current_stage_blocks = stage_manager.current_stage.get_stage()


def draw_stage():
    display.fill(white)
    for block in current_stage_blocks:
        if block.enemy:
            draw_enemy(block)
        else:
            draw_block(block)


def draw_enemy(block):
    pygame.draw.rect(display, black, (block.pos_x - 1, block.pos_y - 1, block.size_x + 2, block.size_y + 2))
    pygame.draw.rect(display, red, (block.pos_x, block.pos_y, block.size_x, block.size_y))


def draw_block(block):
    pygame.draw.rect(display, black, (block.pos_x - 1, block.pos_y - 1, block.size_x + 2, block.size_y + 2))
    pygame.draw.rect(display, white, (block.pos_x, block.pos_y, block.size_x, block.size_y))


def draw_game():
    draw_stage()
    draw_block(player)


def check_next_stage():
    if player.pos_x >= display_width:
        load_next_stage()


def load_next_stage():
    player.go_to_start()
    stage_manager.get_next_stage()


draw_game()
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
                player.move_right()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_SPACE:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                player.stop_jump()
            if event.key == pygame.K_LEFT and player.change_x < 0 \
                    or event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop_x()

    current_stage_blocks = stage_manager.get_stage()
    player.update_pos(current_stage_blocks)
    check_next_stage()

    draw_game()
    pygame.display.update()
    if player.died:
        stage_manager.reset()
        current_stage_blocks = stage_manager.get_stage()
        player.go_to_start()
    clock.tick(60)
