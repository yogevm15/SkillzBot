from elf_kingdom import *
import Default_Values
import constants
def defensive_act(game):
    targetType = None
    target = None
    closestElfToMyElfInDefendRange = None
    closestPortalToMyElfInDefendRange = None
    closestManaFountainToMyElfInDefendRange = None
    for myE in Default_Values.myElves:
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
        if targetType == 0:
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
