import pygame

from src.platformer.blocks.Block import CommonBlocks
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
current_stage_entities = stage_manager.current_stage.get_stage()


def draw_stage():
    display.fill(white)
    for entity in current_stage_entities:
        if entity.enemy:
            draw_enemy(entity)
        else:
            draw_nonenemy(entity)


def draw_enemy(entity):
    pygame.draw.rect(display, red, (entity.pos_x, entity.pos_y, entity.size_x, entity.size_y))


def draw_nonenemy(entity):
    pygame.draw.rect(display, black, (entity.pos_x - 1, entity.pos_y - 1, entity.size_x + 2, entity.size_y + 2))
    pygame.draw.rect(display, white, (entity.pos_x, entity.pos_y, entity.size_x, entity.size_y))


def draw_player():
    pygame.draw.rect(display, black, (player.pos_x - 1, player.pos_y - 1, player.size_x + 2, player.size_y + 2))
    pygame.draw.rect(display, white, (player.pos_x, player.pos_y, player.size_x, player.size_y))


def check_next_stage():
    if player.pos_x >= display_width:
        load_next_stage()


def load_next_stage():
    player.go_to_start()
    stage_manager.get_next_stage()


draw_stage()
draw_player()
pygame.display.update()

game_close = False
while not game_close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_x:
                player.jump()
            if event.key == pygame.K_z:
                print(player.pos_x)
                print(player.pos_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                player.stop_jump()
            if event.key == pygame.K_LEFT and player.change_x < 0 or event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop_x()

    current_stage_entities = stage_manager.get_stage()
    player.update_pos(current_stage_entities)
    check_next_stage()

    draw_stage()
    draw_player()
    pygame.display.update()
    if player.died:
        stage_manager.reset()
        current_stage_entities = stage_manager.get_stage()
        player.go_to_start()
    clock.tick(60)
