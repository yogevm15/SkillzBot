from elf_kingdom import *
import Default_Values
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

        if len(Default_Values.enemyPortals) > 0:
            if e.in_attack_range(closestPortalToElf):
                e.attack(closestPortalToElf)
            else:
                e.move_to(closestPortalToElf)
