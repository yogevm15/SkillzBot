from elf_kingdom import *
import Default_Values
import math
import constants
import invisibilitymanager as invisibility


def get_build_radius(game):
    if len(Default_Values.enemyPortals)>0:
        closestEnemyPortalToMyCastle = Default_Values.enemyPortals[0]
        for p in Default_Values.enemyPortals:
            if p.distance(Default_Values.myCastle) < closestEnemyPortalToMyCastle.distance(Default_Values.myCastle) and p.distance(Default_Values.myCastle)>3000:
                closestEnemyPortalToMyCastle = p
        buildRadius = closestEnemyPortalToMyCastle.distance(Default_Values.enemyCastle)+750
    else:
        buildRadius = constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE
    return buildRadius

def get_build_location(game,elf):
    buildRadius = get_build_radius(game)
    X = Default_Values.enemyCastle.get_location().col + (buildRadius*math.cos((math.pi / 180)*360))
    Y = Default_Values.enemyCastle.get_location().row + (buildRadius*math.sin((math.pi / 180)*360))
    closestAttackLoc = Location(int(Y),int(X))
    for i in range(360,0,-1):
        X = Default_Values.enemyCastle.get_location().col + (buildRadius*math.cos((math.pi / 180)*i))
        Y = Default_Values.enemyCastle.get_location().row + (buildRadius*math.sin((math.pi / 180)*i))
        buildLoc = Location(int(Y), int(X))
        if (game.can_build_portal_at(buildLoc)) and (elf.distance(buildLoc)<elf.distance(closestAttackLoc)):
            closestAttackLoc = buildLoc
    game.debug("[BuildAct]: Elf Try To build attack portal")
    return closestAttackLoc

def build_act(game):
    for e in Default_Values.myElves:
        buildLoc = get_build_location(game,e)
        print buildLoc
        if e.get_location() == buildLoc:
            if e.can_build_portal(): #and isBuildPortalNeeded:
                e.build_portal()
        elif invisibility.check_invisibility(game,e):
            e.cast_speed_up()
        else:
            e.move_to(buildLoc)
