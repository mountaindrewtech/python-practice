class Player:

    def __init__(player, name, timestart, level):
        player.name = name
        player.timestart = timestart
        player.level = level

    def continue_game(player):
        if player.level <= 1:
            return True
        else:
            return False