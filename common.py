defense_range = 0

def update(game):
    global defense_range

    defense_range = game.get_my_castle().distance(game.get_enemy_castle()) / 2
