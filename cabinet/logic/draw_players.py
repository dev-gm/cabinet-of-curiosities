def draw_player(screen, color, coordinate, player_size):
    draw_circle(screen, color, coordinate, player_size)

def draw_players(screen, colors, coordinates, player_size):
    for i in range(len(coordinates)):
        color = colors[i]
        coordinate = coordinates[i]
        draw_player(screen, color, coordinate, player_size)
