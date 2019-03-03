from elf_kingdom import *
import Default_Values
import invisibilitymanager as invisibility
import math

def aggresive_act(game):
    isAttackElfNeeded = True
    closestEnemyEToMyE = None
    closestElfToElf = None
    for e in Default_Values.myElves:
        for ee in Default_Values.enemyElves:
            if ee.distance(e) < 500 and ee.distance(Default_Values.enemyCastle) < 2000:
                closestElfToElf = ee
        if len(Default_Values.enemyElves) >  0 and closestElfToElf is not None:
            closestElfToElf = Default_Values.enemyElves[0]
            for ee in Default_Values.enemyElves:
                if ee.distance(e) < closestElfToElf.distance(e):
                    closestElfToElf = ee
            if e.in_attack_range(closestElfToElf):
                e.attack(closestElfToElf)
            elif invisibility.check_invisibility(game,e):
                e.cast_speed_up()
            else:
                e.move_to(closestElfToElf)
        elif len(Default_Values.enemyManaFountains) > 0:
            closestManaToElf = Default_Values.enemyManaFountains[0]
            for m in Default_Values.enemyManaFountains:
                if m.distance(e) < closestManaToElf.distance(e):
                    closestManaToElf = m
            if e.in_attack_range(closestManaToElf):
                e.attack(closestManaToElf)
            elif invisibility.check_invisibility(game,e):
                e.cast_speed_up()
            else:
                e.move_to(closestManaToElf)
        elif len(Default_Values.enemyPortals) > 0:
            closestPortalToElf = Default_Values.enemyPortals[0]
            for p in Default_Values.enemyPortals:
                if p.distance(e) < closestPortalToElf.distance(e):
                    closestPortalToElf = p
            if e.in_attack_range(closestPortalToElf):
                e.attack(closestPortalToElf)
            elif invisibility.check_invisibility(game,e):
                e.cast_speed_up()
            else:
                e.move_to(closestPortalToElf)
