from elf_kingdom import *
import Default_Values
import Evasion
import math

def aggresive_act(game):
    isAttackElfNeeded = True
    closestEnemyEToMyE = None
    for e in Default_Values.myElves:
        if len(Default_Values.enemyPortals) > 0:
            closestPortalToElf = Default_Values.enemyPortals[0]
            for p in Default_Values.enemyPortals:
                if p.distance(e) < closestPortalToElf.distance(e):
                    closestPortalToElf = p
        evasionResult = Evasion.should_avoid(game,e,closestPortalToElf)

        if evasionResult[0]:
            enemy = evasionResult[1]
            loc = Evasion.get_avoid_location(game, e, enemy)
            if loc.in_map():
                e.move_to()
            else:
                if e.in_attack_range(enemy):
                    e.attack(enemy)
                else:
                    e.move_to(enemy)
        if len(Default_Values.enemyPortals) > 0:
            if e.in_attack_range(closestPortalToElf):
                e.attack(closestPortalToElf)
            else:
                e.move_to(closestPortalToElf)
