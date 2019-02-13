import constants
from elf_kingdom import *
import common
import utils
import build_task

attack_mission_elf = None
buildings_attacked = {}
defense_building_elf = None
current_build_task = None
last_attack_turn = 0
building_mana_fountain = False
balagan = False

def init(game):
    global buildings_attacked
    for elf in game.get_all_my_elves():
        buildings_attacked[elf] = None


def do_turn(game):
    """
    A single turn
    :type game: Game
    """

    if game.turn == 1:
        init(game)

    common.update(game)  # Update common variables

    for elf in game.get_my_living_elves():
        if elf != attack_mission_elf:
            process_defense(game, elf)
        else:
            process_attack(game, elf)

    process_defense_portal(game)
    check_assign_attack(game)


def process_defense(game, elf):
    """
    :type elf: Elf
    :type game: Game
    """

    global buildings_attacked

    buildings_to_destroy = utils.get_enemy_buildings_in_range(game, game.get_my_castle(), common.defense_range)
    utils.sort_by_distance(buildings_to_destroy, elf)

    game.debug("Found Buildings To Destroy: " + str(buildings_to_destroy))

    building_to_attack = buildings_attacked[elf]
    assigned_new = False
    if building_to_attack is None or building_to_attack not in buildings_to_destroy:

        buildings_attacked[elf] = None
        game.debug("Assigning New Building To Destroy!")

        for b in buildings_to_destroy:
            if b not in buildings_attacked.values():
                buildings_attacked[elf] = b
                building_to_attack = b
                assigned_new = True
                game.debug("Successfully Found New Building!")
                break

    if not assigned_new and building_to_attack is None:
        game.debug("No Building To Attack!")
        process_defense_build(game, elf)
    else:
        game.debug("Attacking " + str(building_to_attack))
        if elf.in_attack_range(building_to_attack):
            elf.attack(building_to_attack)
        else:
            elf.move_to(building_to_attack)


def process_defense_build(game, elf):
    global building_mana_fountain
    game.debug("BUILDING MANA FOUNTAIN: " + str(building_mana_fountain))
    task = build_task.get_build_task(game)
    if not task or task.elf != elf:
        process_defense_patrol(game, elf)
    else:
        task.process_building(game)
        building_mana_fountain = not task.complete
    if not task:
        building_mana_fountain = False



def process_defense_patrol(game, elf):
    defend_from = utils.get_to_defend_from(game)
    utils.sort_by_distance(defend_from, elf)

    if len(defend_from) < 1:
        game.debug("Nothing to defend from!")
    else:
        enemy = defend_from[0]
        if enemy.distance(elf) <= common.defense_range:
            if elf.in_attack_range(enemy):
                elf.attack(enemy)
            else:
                elf.move_to(enemy)


def process_defense_portal(game):
    global last_attack_turn
    defense_portal = utils.get_defense_portal(game)
    if defense_portal is None:
        game.debug("[Defense Portal]: No Defense Portal!")
        return

    to_defend = utils.get_to_defend_from(game)
    should_defend = False
    should_defend_from_elf = False
    for enemy in to_defend:
        if enemy.distance(game.get_my_castle()) < constants.DEFENSE_RADIUS:
            should_defend = True
            if enemy is Elf:
                should_defend_from_elf = True

    if (should_defend and game.turn - last_attack_turn > constants.DEFENSE_PORTAL_COOLDOWN or should_defend_from_elf) and not building_mana_fountain:
        defense_portal.summon_ice_troll()
        last_attack_turn = game.turn


def check_assign_attack(game):
    global attack_mission_elf
    if utils.need_defense_portals(game) or utils.need_mana_fountains(game) \
            or len(utils.get_my_dead_elves(game)) != 0 or attack_mission_elf is not None:
        return
    loc = utils.get_attack_portal_loc(game)
    elf = utils.sort_by_distance(game.get_my_living_elves(), loc)[0]
    attack_mission_elf = elf


def process_attack(game, elf):
    global balagan

    loc = utils.get_attack_portal_loc(game)
    if utils.get_attack_portal(game) is None:
        if not elf.location.equals(loc):
            elf.move_to(loc)
        else:
            elf.build_portal()
    else:
        attack_portal = utils.get_attack_portal(game)
        buildings =  utils.get_enemy_buildings_in_range(game, game.get_enemy_castle(), common.defense_range)
        utils.sort_by_importance(buildings)
        if len(buildings) > 0:
            if elf.in_attack_range(buildings[0]):
                elf.attack(buildings[0])
            else:
                elf.move_to(buildings[0])
        else:
            balagan = True
        if balagan:
            attack_portal.summon_lava_giant()


