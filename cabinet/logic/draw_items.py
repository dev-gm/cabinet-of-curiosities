def draw_items(screen, primary, secondary, height, width, items, player_size, item_size):
    rects_list = []
    player_size *= 2
    one = [0, 0]
    two = [width - item_size, 0]
    times = 4
    run = True
    while run:
        draw_rect(screen, primary, (one[0], one[1], item_size, item_size))
        draw_rect(screen, primary, (two[0], two[1], item_size, item_size))
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
    draw_rect(screen, primary, (middle[0], middle[1], item_size, item_size))
    rects_list.append(middle)
    rects = {}
    i = 0
    run = True
    font = SysFont("Arial", int(25*(height/480)))
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
