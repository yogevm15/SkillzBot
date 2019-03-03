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
                game.debug("[MainBot]: Elves Acting Defensive")
                return 2
        for p in Default_Values.enemyPortals:
            if p.distance(Default_Values.myCastle)<constants.RANGE_PORTAL_TO_MY_CASTLE_TO_DEFEND:
                print "[MainBot]: Elves Acting Defensive"
                return 2
        for m in Default_Values.enemyManaFountains:
            if m.distance(Default_Values.myCastle)<constants.RANGE_MANA_FOUNTAIN_TO_MY_CASTLE_TO_DEFEND:
                game.debug("[MainBot]: Elves Acting Defensive")
                return 2

    # Otherwise build
    defensePortal = False
    manaFountains = False
    for p in Default_Values.myPortals:
        if p.distance(Default_Values.myCastle) < constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE+500:
            defensePortal = True
            game.debug("[MainBot]: We Have Defesive Portal")
    if len(Default_Values.myManaFountains)> 1:
        manaFountains = True
        game.debug("[MainBot]: We Have Two Mana Fountains")
    if not manaFountains or not defensePortal:
        game.debug("[MainBot]: Elves Acting Defensive Building")
        return 0
        
    num_attack_portals = 0
    for p in Default_Values.myPortals:
        if p.distance(Default_Values.myCastle) >= 2000:
            num_attack_portals += 1
    
    if num_attack_portals < 1:
        print "[MainBot]: Elves Acting Aggresive Building " + str(num_attack_portals)
        return 1
    game.debug("[MainBot]: We Have At Least One Agressive Portals, Elves Attacking Agressive")
    return 3
def handle_act(game, act):
    if act == 0:
        buildDef.handle_build_act(game)
    elif act == 1:
        buildAgg.build_act(game)
    elif act == 2:
        defense.defensive_act(game)
    else:
        attack.aggresive_act(game)
