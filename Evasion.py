from elf_kingdom import *
import constants
import Evasion
# Returns tuple (is should evade: bool, what to evade: map object)
def should_avoid(game, elf, target):
    avoidable = game.get_enemy_ice_trolls()
    avoidable.extend(game.get_enemy_living_elves())
    elfloc = elf.location
    check_circle_loc = elfloc.towards(target, constants.ELF_ENEMY_CHECK_RAD)

    closest = None
    closest_dist = None
    for e in avoidable:
        eloc = e.location
        dst = eloc.distance(check_circle_loc)
        if(dst < constants.ELF_ENEMY_CHECK_RAD):
            if closest_dist == None or dst < closest_dist:
                closest_dist = dst
                closest = e
    if closest != None:
        print "[Evasion]: Found Enemy To Avoid! " , closest
    else:
        game.debug("[Evasion]: Found Nothing To Avoid!")
    return (closest != None, closest)


# Returns location
def get_avoid_location(game, elf, to_avoid):
    elfloc = elf.location
    avoidloc = to_avoid.location

    final_location = None

    if type(to_avoid) is IceTroll:
        game.debug("[Evasion]: Avoiding Ice Troll!")
        elf_avoid_vec = Location(elf.row - avoidloc.row, elf.col - avoidloc.col)
        final_location = elfloc.add(elf_avoid_vec)
    elif type(to_avoid) is Elf:
        game.debug("[Evasion]: Avoiding Elf!")
        elf_avoid_vec = Location(elf.get_location().row - avoidloc.row, elf.get_location().col - avoidloc.col)
        final_location = elfloc.add(elf_avoid_vec)
    else:
        raise Exception("[Evasion]: Trying to avoid something that isn't an IceTroll or an Elf! I don't know how to avoid [" + type(to_avoid) + "].")

    return final_location
