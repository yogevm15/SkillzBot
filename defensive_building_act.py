from elf_kingdom import *
import Default_Values
import constants


def handle_build_act(game):
    if( len(Default_Values.enemyManaFountains)==0:
        if len(Default_Values.myElves)>1:
            closestElfToManaLoc = Default_Values.myElves[0]
            for e in Default_Values.myElves:
                if e.distance(build_mana_fountain_loc(game))<closestElfToManaLoc.distance(build_mana_fountain_loc(game)):
                    closestElfToManaLoc = e
            for e in Default_Values.myElves:
                if e == closestElfToManaLoc:
                    build_mana(game,e,build_mana_fountain_loc(game))
                else:

    for p in Default_Values.myPortals:
        if p.distance(Default_Values.myCastle) < constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE+100:
            build_mana_fountains(game)
            print "[DefBuildAct]: Elves Building Mana Fountains"



def build_mana(game,elf,loc):
    if(elf.get_location()==closestDefLoc):
        if(elf.can_build_mana_fountain()):
            elf.build_mana_fountain()
    else:
        elf.move_to()





def build_mana_fountain_loc(game):
    X = Default_Values.enemyCastle.get_location().col + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.cos((math.pi / 180)*360))
    Y = Default_Values.enemyCastle.get_location().row + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.sin((math.pi / 180)*360))
    closestDefLoc = Location(Y,X)
    middleLoc = Default_Values.myCastle.towards(Default_Values.enemyCastle,constans.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE)
    for i in range(360,0,-1):
        X = Default_Values.enemyCastle.get_location().col + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.cos((math.pi / 180)*i))
        Y = Default_Values.enemyCastle.get_location().row + (constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE*math.sin((math.pi / 180)*i))
        buildLoc = Location(Y, X)
        if (game.can_build_portal_at(buildLoc)) and (middleLoc.distance(buildLoc)<middleLoc.distance(closestDefLoc)):
            closestDefLoc = buildLoc
    return closestDefLoc
    game.debug("[DefBuildAct]: Elf Try To build mana fountain")






def defend_until_mana_build(game,elf):
    
