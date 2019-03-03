from elf_kingdom import *
import Default_Values
import constants
import math

def handle_build_act(game):
    if len(Default_Values.myManaFountains)<2:
        if len(Default_Values.myElves)>0 and game.get_my_mana()>=130:
            closestElfToManaLoc = Default_Values.myElves[0]
            for e in Default_Values.myElves:
                if e.distance(build_mana_fountain_loc(game))<closestElfToManaLoc.distance(build_mana_fountain_loc(game)):
                    closestElfToManaLoc = e
            for e in Default_Values.myElves:
                if e == closestElfToManaLoc:
                    build_mana(game,e,build_mana_fountain_loc(game))
                else:
                    defend_until_mana_build(game,e)
        else:
            for e in Default_Values.myElves:
                defend_until_mana_build(game,e)
    else:
        if len(Default_Values.myElves)>0 and game.get_my_mana()>=60:
            closestElfToPortalLoc = Default_Values.myElves[0]
            for e in Default_Values.myElves:
                if e.distance(get_portal_loc(game))<closestElfToPortalLoc.distance(get_portal_loc(game)):
                    closestElfToPortalLoc = e
            for e in Default_Values.myElves:
                if e == closestElfToPortalLoc:
                    if e.get_location() == get_portal_loc(game):
                        e.build_portal()
                    else:
                        e.move_to(get_portal_loc(game))
                else:
                    defend_until_mana_build(game,e)
        else:
            for e in Default_Values.myElves:
                defend_until_mana_build(game,e)



def build_mana(game,elf,loc):
    if(elf.get_location()==loc):
        if(elf.can_build_mana_fountain()):
            elf.build_mana_fountain()
    else:
        elf.move_to(loc)


def get_portal_loc(game):
    return Default_Values.myCastle.get_location().towards(Default_Values.enemyCastle.get_location(),constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE)


def build_mana_fountain_loc(game):
    X = Default_Values.myCastle.get_location().col + (constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE*math.cos((math.pi / 180)*360))
    Y = Default_Values.myCastle.get_location().row + (constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE*math.sin((math.pi / 180)*360))
    closestDefLoc = Default_Values.myCastle.get_location().towards(Default_Values.enemyCastle.get_location(),constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE)
    middleLoc = Default_Values.myCastle.get_location().towards(Default_Values.enemyCastle.get_location(),constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE)
    for i in range(360,0,-1):
        X = Default_Values.myCastle.get_location().col + (constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE*math.cos((math.pi / 180)*i))
        Y = Default_Values.myCastle.get_location().row + (constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE*math.sin((math.pi / 180)*i))
        buildLoc = Location(int(Y), int(X))
        if (game.can_build_portal_at(buildLoc)) and (middleLoc.distance(buildLoc)>middleLoc.distance(closestDefLoc)):
            closestDefLoc = buildLoc
    return closestDefLoc
    game.debug("[DefBuildAct]: Elf Try To build mana fountain")






def defend_until_mana_build(game,myE):
    targetType = None
    target = None
    middleLoc = Default_Values.myCastle.get_location().towards(Default_Values.enemyCastle.get_location(),constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE)
    if len(Default_Values.enemyLavaGiants)>0:
        closestLavaToMyElfInDefendRange = Default_Values.enemyLavaGiants[0]
        for enemyL in Default_Values.enemyLavaGiants:
            if enemyL.distance(Default_Values.myCastle)<constants.RANGE_ELF_TO_MY_CASTLE_TO_DEFEND and enemyL.distance(myE)<=closestLavaToMyElfInDefendRange.distance(myE):
                closestLavaToMyElfInDefendRange = enemyL
                targetType = 3
    if len(Default_Values.enemyElves)>0:
        closestElfToMyElfInDefendRange = Default_Values.enemyElves[0]
        for enemyE in Default_Values.enemyElves:
            if enemyE.distance(Default_Values.myCastle)<constants.RANGE_ELF_TO_MY_CASTLE_TO_DEFEND and enemyE.distance(myE)<=closestElfToMyElfInDefendRange.distance(myE):
                closestElfToMyElfInDefendRange = enemyE
                targetType = 0
    if len(Default_Values.enemyPortals)>0:
        closestPortalToMyElfInDefendRange = Default_Values.enemyPortals[0]
        for enemyP in Default_Values.enemyPortals:
            if enemyP.distance(Default_Values.myCastle)<constants.RANGE_PORTAL_TO_MY_CASTLE_TO_DEFEND and enemyP.distance(myE)<=closestPortalToMyElfInDefendRange.distance(myE):
                closestPortalToMyElfInDefendRange = enemyP
                targetType = 1
    if len(Default_Values.enemyManaFountains)>0:
        closestManaFountainToMyElfInDefendRange = Default_Values.enemyManaFountains[0]
        for enemyM in Default_Values.enemyManaFountains:
            if enemyM.distance(Default_Values.myCastle)<constants.RANGE_MANA_FOUNTAIN_TO_MY_CASTLE_TO_DEFEND and enemyM.distance(myE)<=closestManaFountainToMyElfInDefendRange.distance(myE):
                closestManaFountainToMyElfInDefendRange = enemyM
                targetType = 2
    if targetType == None:
        myE.move_to(middleLoc)
    elif targetType == 3:
        target = closestLavaToMyElfInDefendRange
        game.debug("[DefensiveAct]: Target to attack: Lava")
    elif targetType == 0:
        target = closestElfToMyElfInDefendRange
        game.debug("[DefensiveAct]: Target to attack: Elf")
    elif targetType == 1:
        target = closestPortalToMyElfInDefendRange
        game.debug("[DefensiveAct]: Target to attack: Portal")
    else:
        target = closestManaFountainToMyElfInDefendRange
        game.debug("[DefensiveAct]: Target to attack: Mana Fountain  /n")
    if target != None:
        if(myE.in_attack_range(target)):
            myE.attack(target)
        else:
            myE.move_to(target)
