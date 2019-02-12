from elf_kingdom import *
from Default_Values import *

def defensive_act(game):
    targetType = None
    target = None
    closestElfToMyElfInDefendRange = None
    closestPortalToMyElfInDefendRange = None
    closestManaFountainToMyElfInDefendRange = None
    if len(enemyElves)>0:
        closestElfToMyElfInDefendRange = enemyElves[0]
    if len(enemyPortals)>0:
        closestPortalToMyElfInDefendRange = enemyPortals[0]
    if len(enemyManaFountains)>0:
        closestManaFountainToMyElfInDefendRange = enemyManaFountains[0]
    for myE in myElves:
        for enemyE in enemyElves:
            if enemyE.distance(myCastle)<constants.RANGE_ELF_TO_MY_CASTLE_TO_DEFEND and enemyE.distance(myE)<closestElfToMyElfInDefendRange.distance(myE):
                closestElfToMyElfInDefendRange = enemyE
                targetType = 0
        for enemyP in enemyPortals:
            if enemyP.distance(myCastle)<constants.RANGE_ELF_TO_MY_CASTLE_TO_DEFEND and enemyP.distance(myE)<closestPortalToMyElfInDefendRange.distance(myE):
                closestPortalToMyElfInDefendRange = enemyP
                targetType = 1
        for enemyM in enemyManaFountains:
            if enemyM.distance(myCastle)<constants.RANGE_ELF_TO_MY_CASTLE_TO_DEFEND and enemyM.distance(myE)<closestManaFountainToMyElfInDefendRange.distance(myE):
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
            game.debug("[DefensiveAct]: Target to attack: Mana Fountain")
        if Evasion.CheckEvasion(game,myE):
            Evasion.ElfEvasion(game,myE)
        elif myE.in_attack_range(target):
            myE.attack(target)
        else:
            myE.move_to(target)
