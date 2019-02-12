from elf_kingdom import *
from Default_Values import *
import Evasion
import math


def get_build_location(game,elf):
    X = enemyCastle.get_location().col + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.cos((math.pi / 180)*360))
    Y = enemyCastle.get_location().row + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.sin((math.pi / 180)*360))
    closestAttackLoc = Location(Y,X)
    buildLoc = enemyCastle.towards(myCastle,abs(myCastle.get_location().col-enemyCastle.get_location.col)/2)
    aggrsivePortal = False
    for p in myPortals:
        if p.get_location() == buildLoc:
            aggrsivePortal = True
        else:
            game.debug("[BuildAct]: Elf: " + elf + "/nTry To build portal in: " + buildLoc)
            return buildLoc
    if aggrsivePortal:
        for i in range(360,0,-1):
            X = enemyCastle.get_location().col + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.cos((math.pi / 180)*i))
            Y = enemyCastle.get_location().row + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.sin((math.pi / 180)*i))
            buildLoc = Location(Y, X)
            if (game.can_build_portal_at(buildLoc)) and (elf.distance(buildLoc)<elf.distance(closestAttackLoc)):
                closestAttackLoc = buildLoc
    game.debug("[BuildAct]: Elf: " + elf + "/nTry To build portal in: " + closestAttackLoc)
    return closestAttackLoc

def building_act(game):
    for e in myElves:
        buildLoc = get_build_location(game,e)
        evasionResult = Evasion.should_avoid(game, e,buildLoc) # (should evade? )
        if evasionResult[0]:
            enemy = evasionResult[1]
            loc = Evasion.get_avoid_location(game, e, enemy)
            if loc.in_map()
                e.move_to(loc)
            else:
                if e.in_attack_range(enemy):
                    e.attack(enemy)
                else:
                    e.move_to(enemy)
        else:
            if e.get_location() == buildLoc:
                if e.can_build_portal()&&isBuildPortalNeeded:
                    e.build_portal()
            else:
                e.move_to(buildLoc)
