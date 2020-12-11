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
