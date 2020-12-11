def detect_collision(coordinates, rects, item_size, player_size):
    x, y = coordinates
    for name in rects:
        rect = rects.get(name)
        if (x > rect[0] and y > rect[1]) and (x < rect[0] + item_size and y < rect[1] + item_size):
            return name
