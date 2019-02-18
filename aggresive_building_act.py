from elf_kingdom import *
import Default_Values
import math
import constants


def get_build_location(game,elf):
    X = Default_Values.enemyCastle.get_location().col + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.cos((math.pi / 180)*360))
    Y = Default_Values.enemyCastle.get_location().row + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.sin((math.pi / 180)*360))
    closestAttackLoc = Location(Y,X)
    buildLoc = Default_Values.enemyCastle.get_location().towards(Default_Values.myCastle, Default_Values.enemyCastle.distance(Default_Values.myCastle)/2)
    aggrsivePortal = False
    if len(Default_Values.myPortals)>0:
        for p in Default_Values.myPortals:
            if p.get_location() == buildLoc:
                game.debug(buildLoc)
                aggrsivePortal = True
            else:
                game.debug("[BuildAct]: Elf: Try To build middle portal")
                return buildLoc
        if aggrsivePortal:
            for i in range(360,0,-1):
                X = Default_Values.enemyCastle.get_location().col + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.cos((math.pi / 180)*i))
                Y = Default_Values.enemyCastle.get_location().row + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.sin((math.pi / 180)*i))
                buildLoc = Location(Y, X)
                if (game.can_build_portal_at(buildLoc)) and (elf.distance(buildLoc)<elf.distance(closestAttackLoc)):
                    closestAttackLoc = buildLoc
        game.debug("[BuildAct]: Elf Try To build attack portal")
        return closestAttackLoc
    else:
        return buildLoc

def build_act(game):
    for e in Default_Values.myElves:
        buildLoc = get_build_location(game,e)
        if e.get_location() == buildLoc:
            if e.can_build_portal(): #and isBuildPortalNeeded:
                e.build_portal()
        else:
            e.move_to(buildLoc)
