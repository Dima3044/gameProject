from enviroment import Maze, Enemy
import pygame
from player import Player

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 300))

zombie_img = pygame.image.load('images/zombie.png')
maze = Maze()
enemy = Enemy()
enemy.addEnemy(zombie_img, (144, 144))
enemy.addEnemy(zombie_img, (288, 240))
enemy.addEnemy(zombie_img, (352, 1008))
enemy.addEnemy(zombie_img, (800, 528))
player_obj = Player()

label = pygame.font.Font('fonts/Roboto_Condensed-Black.ttf', 15)


running = True
while running:
    maze.moveEnemies()
    maze.drawMap(screen)
    maze.drawInventory(screen)
    keys = pygame.key.get_pressed()
    player_obj.move(maze, keys)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(15)
