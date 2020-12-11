import pygame

width = 800
height = 575

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cabinet of Curiosities")

from cabinet.run import game, lobby
from cabinet.constants import get_colors


increase = height/480


clock = pygame.time.Clock()
fps = 24

player_size = int(30*increase)
item_size = int(75*increase)

black, white, red, green, blue = get_colors()
colors = (red, green)
background = white
text = black

lobby(background, text, colors, player_size, height)
game(screen, background, colors, player_size, item_size, (width, height))



