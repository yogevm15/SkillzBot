from elf_kingdom import *
import Default_Values
import constants

import aggresive_building_act as buildAgg
import defensive_building_act as buildDef
import aggresive_act as attack
import defensive_act as defense
import mana as mana

def do_turn(game):
    Default_Values.init(game)
    act = best_act(game)
    manaReport = mana.handle_mana(game,0);
    handle_act(game, act)

def best_act(game):
    # Check if should act agressively (if there are at least 2 attack portals)
    num_attack_portals = 0
    for p in Default_Values.myPortals:
        if p.distance(Default_Values.enemyCastle) < constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE + 100:
            num_attack_portals += 1

    if num_attack_portals > 1:
        game.debug("[MainBot]: We Have At Least Two Agressive Portals, Elves Attacking Agressive")
        return 3


    # Check if should act defensively
    if len(Default_Values.enemyElves) > 0 or len(Default_Values.enemyPortals) > 0 or len(Default_Values.enemyManaFountains) > 0:
        if len(Default_Values.enemyElves) > 0:
            closestEnemyToCastle = Default_Values.enemyElves[0]
        elif len(Default_Values.enemyPortals) > 0:
            closestEnemyToCastle = Default_Values.enemyPortals[0]
        else:
            closestEnemyToCastle = Default_Values.enemyManaFountains[0]


        for e in Default_Values.enemyElves:
            if e.distance(Default_Values.myCastle)<constants.RANGE_ELF_TO_MY_CASTLE_TO_DEFEND:
                game.debug("[MainBot]: Elves Acting Defensive elf")
                return 2
        for p in Default_Values.enemyPortals:
            if p.distance(Default_Values.myCastle)<constants.RANGE_PORTAL_TO_MY_CASTLE_TO_DEFEND:
                print "[MainBot]: Elves Acting Defensive"
                return 2
        for m in Default_Values.enemyManaFountains:
            if m.distance(Default_Values.myCastle)<constants.RANGE_MANA_FOUNTAIN_TO_MY_CASTLE_TO_DEFEND:
                game.debug("[MainBot]: Elves Acting Defensive mana")
                return 2

    # Otherwise build
    defensePortal = False
    manaFountains = False
    for p in Default_Values.myPortals:
        if p.distance(Default_Values.myCastle) < constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE+100:
            defensePortal = true
            game.debug("[MainBot]: We Have Defesive Portal")
    if len(Default_Values.enemyManaFountains)>1:
        manaFountains = True
        game.debug("[MainBot]: We Have Two Mana Fountains")
    if manaFountains and defensePortal:
        game.debug("[MainBot]: Elves Acting Aggresive Building")
        return 1
    else:
        game.debug("[MainBot]: Elves Acting Defensive Building")
        return 0

def handle_act(game, act):
    if act == 0:
        buildDef.build_act(game)
    elif act == 1:
        buildAgg.build_act(game)
    elif act == 2:
        defense.defensive_act(game)
    else:
        attack.agressive_act(game)
