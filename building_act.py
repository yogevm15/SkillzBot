from elf_kingdom import *
from Default_Values import *
import Evasion
import math
import constants


def get_build_location(game,elf):
    enemyPortals = game.get_enemy_portals()
    enemyElves = game.get_enemy_living_elves()
    enemyCastle = game.get_enemy_castle()
    enemyIceTrolls = game.get_enemy_ice_trolls()
    enemyLavaGiants = game.get_enemy_lava_giants()
    enemyManaFountains = game.get_enemy_mana_fountains()
    myCastle = game.get_my_castle()
    myPortals = game.get_my_portals()
    myManaFountains = game.get_my_mana_fountains()
    myElves = game.get_my_living_elves()
    myIceTrolls = game.get_my_ice_trolls()
    X = enemyCastle.get_location().col + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.cos((math.pi / 180)*360))
    Y = enemyCastle.get_location().row + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.sin((math.pi / 180)*360))
    closestAttackLoc = Location(Y,X)
    buildLoc = enemyCastle.get_location().towards(myCastle, enemyCastle.distance(myCastle)/2)
    aggrsivePortal = False
    if len(myPortals)>0:
        for p in myPortals:
            if p.get_location() == buildLoc:
                game.debug(buildLoc)
                aggrsivePortal = True
            else:
                game.debug("[BuildAct]: Elf: Try To build middle portal")
                return buildLoc
        if aggrsivePortal:
            for i in range(360,0,-1):
                X = enemyCastle.get_location().col + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.cos((math.pi / 180)*i))
                Y = enemyCastle.get_location().row + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.sin((math.pi / 180)*i))
                buildLoc = Location(Y, X)
                if (game.can_build_portal_at(buildLoc)) and (elf.distance(buildLoc)<elf.distance(closestAttackLoc)):
                    closestAttackLoc = buildLoc
        game.debug("[BuildAct]: Elf Try To build attack portal")
        return closestAttackLoc
    else:
        return buildLoc

def build_act(game):
    enemyPortals = game.get_enemy_portals()
    enemyElves = game.get_enemy_living_elves()
    enemyCastle = game.get_enemy_castle()
    enemyIceTrolls = game.get_enemy_ice_trolls()
    enemyLavaGiants = game.get_enemy_lava_giants()
    enemyManaFountains = game.get_enemy_mana_fountains()
    myCastle = game.get_my_castle()
    myPortals = game.get_my_portals()
    myManaFountains = game.get_my_mana_fountains()
    myElves = game.get_my_living_elves()
    myIceTrolls = game.get_my_ice_trolls()
    for e in myElves:
        buildLoc = get_build_location(game,e)
        evasionResult = Evasion.should_avoid(game, e,buildLoc) # (should evade? )
        if evasionResult[0]:
            enemy = evasionResult[1]
            loc = Evasion.get_avoid_location(game, e, enemy)
            if loc.in_map():
                e.move_to(loc)
            else:
                if e.in_attack_range(enemy):
                    e.attack(enemy)
                else:
                    e.move_to(enemy)
        else:
            if e.get_location() == buildLoc:
                if e.can_build_portal(): #and isBuildPortalNeeded:
                    e.build_portal()
            else:
                e.move_to(buildLoc)
