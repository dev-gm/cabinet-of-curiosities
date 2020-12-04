import pygame, sys
from random import shuffle


def draw_player(screen, color, coordinates, player_size):
    pygame.draw.circle(screen, color, coordinates, player_size)


def draw_items(screen, primary, secondary, height, width, items, player_size, item_size):
    rects_list = []
    player_size *= 2
    one = [0, 0]
    two = [width - item_size, 0]
    times = 4
    run = True
    while run:
        pygame.draw.rect(screen, primary, (one[0], one[1], item_size, item_size))
        pygame.draw.rect(screen, primary, (two[0], two[1], item_size, item_size))
        rects_list.append((one[0], one[1]))
        rects_list.append((two[0], two[1]))
        one[1] += (player_size + item_size)
        two[1] += (player_size + item_size)
        times -= 1
        if times <= 0:
            run = False
        if one[1] > height or two[1] > height:
            run = False
    middle = ((width / 2) - (item_size / 2), (height / 2) - (item_size / 2))
    pygame.draw.rect(screen, primary, (middle[0], middle[1], item_size, item_size))
    rects_list.append(middle)
    rects = {}
    i = 0
    run = True
    font = pygame.font.SysFont("Arial", int(25*(height/480)))
    while i < len(items) and i < len(rects_list):
        name = items[i]
        rects[name] = rects_list[i]
        rect = rects_list[i]
        screen.blit(font.render(name, True, secondary), rect)
        i += 1
        if name == "charlie":
            screen.blit(font.render("card", True, secondary), (rect[0], rect[1]+(item_size/2-item_size/6)))
        elif name == "ear":
            screen.blit(font.render("buds", True, secondary), (rect[0], rect[1]+(item_size/2-item_size/6)))
    return rects


def detect_collision(x, y, rects, item_size, player_size):
    for name in rects:
        rect = rects.get(name)
        if (x > rect[0] and y > rect[1]) and (x < rect[0] + item_size and y < rect[1] + item_size):
            return name


def check_limits(number, minimum, maximum, radius):
    minimum += radius
    maximum -= radius
    if number < minimum:
        number = minimum
    elif number > maximum:
        number = maximum
    return number


pygame.init()

items_list = [
    "gavel", "pen", "pc", "pin", "usb", "phone", "ear", "crocs", "charlie"
]

shuffle(items_list)

width = 800
height = 575

increase = height/480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cabinet of Curiosities")

clock = pygame.time.Clock()
fps = 24

black = (0, 0, 0)
white = (255, 255, 255)
red = (185, 0, 0)
blue = (0, 0, 255)

lobby_background = black
lobby_text = white
background = white

player_size = int(30*increase)
item_size = int(75*increase)

x = int(width / 2)
y = int(height - player_size)

movement = int(50 * increase)

screen.fill(background)
rects = draw_items(screen, blue, white, height, width, items_list, player_size, item_size)

images = {}
for name in rects.keys():
    image = pygame.image.load("images/{}.jpg".format(name))
    size = image.get_size()
    sc = list(size)
    if name == "crocs":
        sc[1] = int(width/(size[0]/size[1])/1.2)
        sc[0] = int(width/1.2)
    elif size[0] > size[1]:
        sc[1] = int(width/(size[0]/size[1]))
        sc[0] = width
    else:
        sc[0] = int(height/(size[1]/size[0]))
        sc[1] = height
    image = pygame.transform.scale(image, tuple(sc))
    images[name] = image

draw_player(screen, red, (x, y), player_size)
prev = [None, None]
pressed = False
while True:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= movement
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= movement
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += movement
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += movement
    x = check_limits(x, 0, width, player_size)
    y = check_limits(y, 0, height, player_size)
    collided = detect_collision(x, y, rects, item_size, player_size)
    print(collided)
    draw_items(screen, blue, white, height, width, items_list, player_size, item_size)
    draw_player(screen, red, (x, y), player_size)
    if collided:
        screen.fill(background)
        screen.blit(images[collided], (0, 0))
    pygame.display.update()

