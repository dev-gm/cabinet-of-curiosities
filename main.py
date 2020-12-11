import pygame, sys
from random import shuffle


def run_lobby(background, text_color, colors, player_size, height):
    right_color, left_color = colors
    player_size = int(player_size * 1.5)
    left_text = ['PLAYER 1:', '', 'To play this game,', 'use the WASD keys', 'to move around.', '', 'Press SPACE to start']
    right_text = ['PLAYER 2:', '', 'To play this game,', 'use the arrow keys', 'to move around.', '', 'Press RETURN to start']
    font_size = 30*(height/480)
    font = pygame.font.SysFont("Arial", int(font_size))
    left_pressed, right_pressed = False, False
    run = True
    while run:
        pygame.display.update()
        screen.fill(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    left_pressed = not left_pressed
                if event.key == pygame.K_RETURN:
                    right_pressed = not right_pressed
        if left_pressed and right_pressed:
                    run = False
        if left_pressed:
            pygame.draw.circle(screen, left_color, (int(width/4), height-item_size), player_size)
        else:
            pygame.draw.circle(screen, left_color, (int(width/4), height-item_size), player_size, 3)
        if right_pressed:
            pygame.draw.circle(screen, right_color, (int(width*(3/4)), height-item_size), player_size)
        else:
            pygame.draw.circle(screen, right_color, (int(width*(3/4)), height-item_size), player_size, 3)
        x, y = font_size - font_size/3, 35
        for text in left_text:
            screen.blit(font.render(text, True, text_color), (y, x))
            x += font_size + font_size/3
        x, y = font_size - font_size/3, width/2 + 35
        for text in right_text:
            screen.blit(font.render(text, True, text_color), (y, x))
            x += font_size + font_size /3

def calc_images(rects):
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
    return images

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

def detect_collision(coordinates, rects, item_size, player_size):
    x, y = coordinates
    for name in rects:
        rect = rects.get(name)
        if (x > rect[0] and y > rect[1]) and (x < rect[0] + item_size and y < rect[1] + item_size):
            return name

def check_limit(number, minimum, maximum, radius):
    minimum += radius
    maximum -= radius
    if number < minimum:
        number = minimum
    elif number > maximum:
        number = maximum
    return number

def check_limits(players, minimum, maximum, radius):
    output = []
    for player in players:
        player[0] = check_limit(player[0], minimum, maximum, radius)
        player[1] = check_limit(player[1], minimum, maximum, radius)
        output.append(player)
    return output

pygame.init()

items = [
    "gavel", "pen", "pc", "pin", "usb", "phone", "ear", "crocs", "charlie"
]

shuffle(items)

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
green = (20, 185, 20)
blue = (0, 0, 255)

player_size = int(30*increase)
item_size = int(75*increase)
colors = (red, green)
background = white
text = black

run_lobby(background, text, colors, player_size, height)

one = [int(width/2) + player_size, int(height - player_size)]
two = [int(width/2) - player_size, int(height - player_size)]
movement = int(50 * increase)

screen.fill(background)
rects = draw_items(screen, blue, white, height, width, items, player_size, item_size)
images = calc_images(rects)

draw_player(screen, colors[0], one, player_size)
draw_player(screen, colors[1], two, player_size)
movement = int(50 * increase)

screen.fill(background)
rects = draw_items(screen, blue, white, height, width, items, player_size, item_size)
images = calc_images(rects)

while True:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                one[1] -= movement
            if event.key == pygame.K_LEFT:
                one[0] -= movement
            if event.key == pygame.K_DOWN:
                one[1] += movement
            if event.key == pygame.K_RIGHT:
                one[0] += movement
            if event.key == pygame.K_w or event.key == pygame.K_COMMA:
                two[1] -= movement
            if event.key == pygame.K_a:
                two[0] -= movement
            if event.key == pygame.K_s or event.key == pygame.K_o:
                two[1] += movement
            if event.key == pygame.K_d or event.key == pygame.K_e:
                two[0] += movement
    one, two = check_limits((one, two), 0, width, player_size)
    collided = [detect_collision(one, rects, item_size, player_size), detect_collision(two, rects, item_size, player_size)]
    print(collided)
    draw_items(screen, blue, white, height, width, items, player_size, item_size)
    draw_player(screen, colors[0], one, player_size)
    draw_player(screen, colors[1], two, player_size)
    for collision in collided:
        if collision:
            screen.fill(background)
            screen.blit(images[collision], (0, 0))
    pygame.display.update()
