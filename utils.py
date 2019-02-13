"""
    game - The game instance
    range_of - The GameObject to check around
    range - The range to check around
"""
def get_enemy_buildings_in_range(game, range_of, range):
    buildings = game.get_enemy_portals()
    buildings.extend(game.get_enemy_mana_fountains())
    output = []
    for b in buildings:
        if range_of.in_range(b, range):
            output.append(b)
    return output

def sort_by_distance(to_sort, distance_from):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(to_sort) - 1):
            d1 = to_sort[i].distance(distance_from)
            d2 = to_sort[i+1].distance(distance_from)
            if d2 < d1:
                to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
                sorted = False
