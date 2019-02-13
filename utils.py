import constants
from elf_kingdom import *

def get_enemy_buildings_in_range(game, range_of, range):
    """
        :param game - The game instance
        :param range_of - The GameObject to check around
        :param range - The range to check around
    """
    buildings = game.get_enemy_portals()
    buildings.extend(game.get_enemy_mana_fountains())
    output = []
    for b in buildings:
        if range_of.in_range(b, range):
            output.append(b)
    return output


def sort_by_distance(to_sort, distance_from):
    """
    :param to_sort: The list to sort
    :param distance_from: the place to measure distance from
    :return The list for chaining
    """

    sorted_by_distance = False
    while not sorted_by_distance:
        sorted_by_distance = True

        for i in range(len(to_sort) - 1):
            d1 = to_sort[i].distance(distance_from)
            d2 = to_sort[i+1].distance(distance_from)
            if d2 < d1:
                to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
                sorted_by_distance = False

    return to_sort


def get_to_defend_from(game):
    output = game.get_enemy_lava_giants()
    output.extend(game.get_enemy_living_elves())
    return output


def need_mana_fountains(game):
    return len(game.get_my_mana_fountains()) < constants.MANA_FOUNTAINS


def need_defense_portals(game):
    return len(game.get_my_portals()) < constants.DEFENSE_PORTALS


def get_defense_portal(game):
    if len(game.get_my_portals()) < 1:
        return None
    return sort_by_distance(game.get_my_portals(), game.get_my_castle())[0]


def get_my_dead_elves(game):
    elves = []
    for elf in game.get_all_my_elves():
        if not elf.is_alive():
            elves.append(elf)
    return elves


def get_attack_portal_loc(game):
    return game.get_my_castle().get_location().towards(game.get_enemy_castle(), game.get_my_castle().distance(game.get_enemy_castle()) / 2)


def get_attack_portal(game):
    if len(game.get_my_portals()) < 2:
        game.debug("[Attack Portal Finder]: No Attack Portal!")
        return None
    return sort_by_distance(game.get_my_portals(), game.get_my_castle())[-1]


def sort_by_importance(buildings, strength = (ManaFountain, Portal)):
    buildings_sorted = False
    while not buildings_sorted:
        buildings_sorted = True
        for i in range(len(buildings)-1):
            b1 = buildings[i].__class__
            b2 = buildings[i+1].__class__
            if strength.index(b1) > strength.index(b2):
                buildings[i], buildings[i+1] = buildings[i+1], buildings[i]
                buildings_sorted = False
    return buildings


def list_contains_type(lst, t):
    for i in lst:
        if i.__class__ is t:
            return True
    return False