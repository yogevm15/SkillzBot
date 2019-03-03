from elf_kingdom import *
import constants
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
    if avoidloc.col-elf.get_location().col == 0:
        X = elf.get_location().col+100
        Y = elf.get_location().row
        final_location = Location(int(Y),int(X))
    elif avoidloc.row-elf.get_location().row ==0:#< avoidloc.col-elf.get_location().col:
        X = elf.get_location().col
        Y = elf.get_location().row+100
        final_location = Location(int(Y),int(X))
    else:
        if type(to_avoid) is IceTroll:
            game.debug("[Evasion]: Avoiding Ice Troll!")
            m = float(avoidloc.row-elf.get_location().row)/(avoidloc.col-elf.get_location().col)
            print avoidloc.row-elf.get_location().row , avoidloc.col-elf.get_location().col, m
            m = m
            X = elf.get_location().col+100
            Y = elf.get_location().row+m*100
            final_location = Location(int(Y),int(X))
        elif type(to_avoid) is Elf:
            game.debug("[Evasion]: Avoiding Elf!")
            m = float(avoidloc.row-elf.get_location().row)/(avoidloc.col-elf.get_location().col)
            m = -1/m
            X = elf.get_location().col+100
            Y = elf.get_location().row+m*100
            final_location = Location(int(Y),int(X))

    return final_location
