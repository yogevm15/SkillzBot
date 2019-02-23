from elf_kingdom import *
from math import *
import constants

last_portals = None

def do_turn(game):
    global last_portals

    for e in game.get_my_living_elves():
        handle_elf(game, e)

    handle_portals(game)
    last_portals = game.get_my_portals()

def handle_elf(game, elf):
    need_mana = len(game.get_my_mana_fountains()) < constants.MANA_FOUTAINS

    if need_mana and elf.can_build_mana_fountain():
        elf.build_mana_fountain()
    elif not need_mana and elf.can_build_portal() and len(game.get_my_portals()) < constants.MAX_PORTALS:
        elf.build_portal()
    else:
        elf.move_to(game.get_enemy_castle())


def handle_portals(game):
    portals = game.get_my_portals()
    if len(portals) < 1:
        game.debug("[Portals] No Portals!")
        return

    for p in get_portals_under_attack(game):
        p.summon_ice_troll()

    portalsScores = []
    for p in portals:
        score = 0
        vec = get_vec(p.location, game.get_enemy_castle().location)
        dst = p.distance(game.get_enemy_castle())

        for ice in game.get_enemy_ice_trolls():
            if distance_from_vec(vec, ice.location) < dst / 4:
                score += 2
        portalsScores.append(score)

    game.debug("[Portals] Given all portals scores:" + str(portalsScores))
    lowest = portalsScores.index(min(portalsScores))
    score = portalsScores[lowest]

    candidates = []
    for i in range(len(portalsScores)):
        if portalsScores[i] < 4:
            candidates.append(i)

    closestI = None
    for i in candidates:
        if closestI is None or portals[i].distance(game.get_enemy_castle()) < portals[closestI].distance(game.get_enemy_castle()):
            closestI = i

    if closestI is not None and should_summon_lava(game, portals[closestI]):
        portals[closestI].summon_lava_giant()

def get_portals_under_attack(game):
    if last_portals is None:
        return []

    under_attack = []
    for p in game.get_my_portals():
        if p in last_portals:
            if p.current_health < last_portals[last_portals.index(p)].current_health:
                under_attack.append(p)
                game.debug("[UnderAttack] Portal " + str(p) + " under attack!")

    return under_attack

# Checks stuff
def should_summon_lava(game, portal):
    max_portals = len(game.get_my_portals()) >= constants.MAX_PORTALS
    can_build_later = game.get_my_mana() - game.portal_cost - game.lava_giant_cost > 0

    return max_portals or can_build_later

# Returns (m,b) from y=mx+b between loc1 and loc2
def get_vec(loc1, loc2):
    m = (loc2.row - loc1.row) / (loc2.col - loc1.col)
    b = loc1.row - m * loc1.col
    return (m, b)

def distance_from_vec(line, loc):
    return (line[0] * loc.col + loc.row - line[1]) / (sqrt(line[0] ** 2 + 1))
