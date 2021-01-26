import pygame

from src.platformer.entities.Entity import Entity
from src.platformer.entities.Player import Player

pygame.init()
display_width = 600
display_height = 400
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

floor = Entity(display_width, display_height - 300, 0, 300, False)
player_size = 20
player_y_max = floor.pos_y - player_size
player = Player(player_size, player_size, 20, player_y_max)

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)

current_stage_entities = []


def draw_stage():
    display.fill(white)
    pygame.draw.line(display, black, (0, floor.pos_y), (display_width, floor.pos_y))
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


def get_entities():
    platform1 = Entity(50, 100, 300, floor.pos_y - 100, False)
    return [platform1]


def check_floor_and_wall_collision():
    if player.pos_y >= player_y_max:
        player.land()
        player.pos_y = player_y_max

    if player.pos_x < 0:
        player.pos_x = 0
    elif player.pos_x > display_width - player.size_x:
        player.pos_x = display_width - player.size_x


draw_stage()
draw_nonenemy(player)
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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                player.stop_jump()
            if event.key == pygame.K_LEFT and player.change_x < 0 or event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop_x()

    current_stage_entities = get_entities()
    player.update_pos(current_stage_entities)
    check_floor_and_wall_collision()

    draw_stage()
    draw_nonenemy(player)
    pygame.display.update()
    clock.tick(60)
