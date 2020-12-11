def lobby(screen, background, text_color, colors, player_size, height):
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