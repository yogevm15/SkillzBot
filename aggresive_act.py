from elf_kingdom import *
from Default_Values import *
import Evasion
import math

def aggresive_act(game):
    enemyPortals = game.get_enemy_portals()
    enemyElves = game.get_enemy_living_elves()
    enemyCastle = game.get_enemy_castle()
    enemyIceTrolls = game.get_enemy_ice_trolls()
    enemyLavaGiants = game.get_enemy_lava_giants()
    enemyManaFountains = game.get_enemy_mana_fountains()
    myCastle = game.get_my_castle()
    myPortals = game.get_my_portals()
    myManaFountains = game.get_my_mana_fountains()
    myElves = game.get_my_living_elves()
    myIceTrolls = game.get_my_ice_trolls()
    isAttackElfNeeded = True
    closestEnemyEToMyE = None
    for e in myElves:
        if len(enemyPortals) > 0:
            closestPortalToElf = enemyPortals[0]
            for p in enemyPortals:
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
        if len(enemyPortals) > 0:
            if e.in_attack_range(closestPortalToElf):
                e.attack(closestPortalToElf)
            else:
                e.move_to(closestPortalToElf)
