from elf_kingdom import *
from Default_Values import *
import constants

import building_act as build
import aggresive_act as attack
import defensive_act as defense

def do_turn(game):
    global manaReport
    Default_Values.init(game)
    act = best_act(game)
    manaReport = ManaClass.HandleMana(game);
    handle_act(game, act)

def best_act(game):


    # Check if should act agressively (if there are at least 2 attack portals)
    num_attack_portals = 0
    for p in myPortals:
        if p.distance(enemyCastle) < constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE + 100:
            num_attack_portals += 1

    if num_attack_portals > 1:
        game.debug("[MainBot]: We Have At Least Two Agressive Portals, Elves Attacking Agressive")
        return 2


    # Check if should act defensively
    if len(enemyElves) > 0 or len(enemyPortals) > 0 or len(enemyManaFountains) > 0:
        if len(enemyElves) > 0:
            closestEnemyToCastle = enemyElves[0]
        elif len(enemyPortals) > 0:
            closestEnemyToCastle = enemyPortals[0]
        else:
            closestEnemyToCastle = enemyManaFountains[0]


        for e in enemyElves:
            if e.distance(myCastle)<constants.RANGE_ELF_TO_MY_CASTLE_TO_DEFEND:
                game.debug("[MainBot]: Elves Acting Defensive")
                return 1
        for p in enemyPortals:
            if p.distance(myCastle)<constants.RANGE_PORTAL_TO_MY_CASTLE_TO_DEFEND:
                game.debug("[MainBot]: Elves Acting Defensive")
                return 1
        for m in enemyManaFountains:
            if m.distance(myCastle)<constants.RANGE_MANA_FOUNTAIN_TO_MY_CASTLE_TO_DEFEND:
                game.debug("[MainBot]: Elves Acting Defensive")
                return 1

    # Otherwise build
    game.debug("[MainBot]: Elves Acting Building")
    return 0

def handle_act(game, act):
    if act == 0:
        build.build_act(game)
    elif act == 1:
        defense.defensive_act(game)
    else:
        attack.agressive_act(game)
