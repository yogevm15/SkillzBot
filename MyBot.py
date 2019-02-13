from elf_kingdom import *
import common
import utils
import constants

attack_mission_elf = None
buildings_attacked = {}
defense_building_elf = None

def init(game):
    global buildings_attacked
    for elf in game.get_all_my_elves():
        buildings_attacked[elf] = None

def do_turn(game):
    if game.turn == 1:
        init(game)

    common.update(game)  # Update common variables

    for elf in game.get_my_living_elves():
        if elf != attack_mission_elf:
            process_defense(game, elf)
        else:
            process_attack(game, elf)

def process_defense(game, elf):
    global buildings_attacked

    buildings_to_destroy = utils.get_enemy_buildings_in_range(game, game.get_my_castle(), common.defense_range)
    utils.sort_by_distance(buildings_to_destroy, elf)

    game.debug("Found Buildings To Destroy: " + str(buildings_to_destroy))

    building_to_attack = buildings_attacked[elf]
    assigned_new = False
    if building_to_attack == None or building_to_attack not in buildings_to_destroy:

        buildings_attacked[elf] = None
        game.debug("Assigning New Building To Destroy!")
        # Find non assigned building
        for b in buildings_to_destroy:
            if not b in buildings_attacked.values():
                buildings_attacked[elf] = b
                building_to_attack = b
                assigned_new = True
                break
    if not assigned_new and building_to_attack == None:
        process_defense_build(game, elf)
    else:
        game.debug("Destroying " + str(building_to_attack))
        if elf.in_attack_range(building_to_attack):
            elf.attack(building_to_attack)
        else:
            elf.move_to(building_to_attack)


def process_defense_build(game, elf):
    global defense_building_elf
    if defense_building_elf == None or defense_building_elf == elf:
        defense_building_elf = elf
        game.debug("Building!")
    else:
        process_defense_patrol(game, elf)

def process_defense_patrol(game, elf):
    pass

def process_attack(game, elf):
    pass
