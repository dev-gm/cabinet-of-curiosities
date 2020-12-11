def game(screen, background, colors, player_size, item_size, screen_size):
    items = get_items()
    width, height = screen_size
    one = [int(width/2) + player_size, int(height - player_size)]
    two = [int(width/2) - player_size, int(height - player_size)]
    increase = height/480
    movement = int(50 * increase)
    black, white, red, green, blue = get_colors()
    screen.fill(background)
    rects = draw_items(screen, blue, white, height, width, items, player_size, item_size)
    images = calc_images(rects)
    draw_players(screen, colors, (one, two), player_size)
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
        draw_players(screen, colors, (one, two), player_size)
        for collision in collided:
            if collision:
                screen.fill(background)
                screen.blit(images[collision], (0, 0))
        pygame.display.update()
