import pygame

from src.platformer.Entity import Entity

pygame.init()
display_width = 600
display_height = 400
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

floor = 300
player_size = 20
player_y_max = floor - player_size
player = Entity(player_size, player_size, 20, player_y_max, False)

change_X = 0
change_Y = 0
grounded = True
gravity = 1
jump_force = -17
movement_speed = 5

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)

game_close = False


def draw_stage():
    display.fill(white)
    pygame.draw.line(display, black, (0, floor), (display_width, floor), 1)


def draw_enemy(entity):
    pygame.draw.rect(display, red, (entity.pos_x, entity.pos_y, entity.size_x, entity.size_y))


def draw_nonenemy(entity):
    pygame.draw.rect(display, black, (entity.pos_x, entity.pos_y, entity.size_x, entity.size_y))


def draw_player():
    pygame.draw.rect(display, black, (player.pos_x - 1, player.pos_y - 1, player.size_x + 2, player.size_y + 2))
    pygame.draw.rect(display, white, (player.pos_x, player.pos_y, player.size_x, player.size_y))


draw_stage()
draw_player()
pygame.display.update()

while not game_close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_X = movement_speed
            if event.key == pygame.K_LEFT:
                change_X = -movement_speed
            if event.key == pygame.K_x:
                if grounded:
                    grounded = False
                    change_Y = jump_force

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                if change_Y < 0:
                    change_Y = 0
            if event.key == pygame.K_LEFT and change_X < 0:
                change_X = 0
            if event.key == pygame.K_RIGHT and change_X > 0:
                change_X = 0

    if not grounded:
        player.pos_y += change_Y
        change_Y += gravity

    if player.pos_y >= player_y_max:
        grounded = True
        player.pos_y = player_y_max
        change_Y = 0

    player.pos_x += change_X
    if player.pos_x < 0:
        player.pos_x = 0
    elif player.pos_x > display_width - player.size_x:
        player.pos_x = display_width - player.size_x

    draw_stage()
    draw_player()
    pygame.display.update()
    clock.tick(60)
