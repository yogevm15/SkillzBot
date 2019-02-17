from elf_kingdom import *
import constants

building = None

def do_turn(game): # {
    # Find Target
    # All Elves Go To It
    # If They Can They Build.
    global building
    building = None

    for elf in game.get_my_living_elves():
        target = find_target(game,elf)
        process_elf(game, elf, target)

    # Portals:
    # Closest to enemy castle summons lava giants
    process_portals(game)

# }

def find_target(game,elf):
    """
        Finds the target for the elves to attack
        game - The game instance
    """
    closest_build_to_elf = None
    if len(game.get_enemy_mana_fountains())>0:
        closest_build_to_elf = game.get_enemy_mana_fountains()[0]
    if len(game.get_enemy_portals())>0:
        closest_build_to_elf = game.get_enemy_portals()[0]
    for m in game.get_enemy_mana_fountains():
        if m.distance(elf)<closest_build_to_elf.distance(elf):
            closest_build_to_elf = m
    for p in game.get_enemy_portals():
        if p.distance(elf)<closest_build_to_elf.distance(elf):
            closest_build_to_elf = p
    if closest_build_to_elf is not None:
        return closest_build_to_elf #return closest build
    else:
        return game.get_enemy_castle() #return enemy castle


def process_elf(game, elf, target): # {
    """
        Processes an elf:
        if the elf can build the desired building she builds it, if enemy elf in range and she have less HP then our elf move to and attack, otherwise she moves toward the castle

        game - The game instance
        elf - The elf
        target - The target to which the elf should go
    """
    global building

    elves_in_range = []
    closest_elf_to_elf = None
    for e in game.get_enemy_living_elves():
        if elf.in_attack_range(e):
            elves_in_range.append(e)
    if len(elves_in_range)>0:
        closest_elf_to_elf = elves_in_range[0]
        for e in elves_in_range:
            if e.distance(elf) < closest_elf_to_elf.distance(elf):
                closest_elf_to_elf = e
    if closest_elf_to_elf is not None:
        if elf.in_attack_range(closest_elf_to_elf):
            elf.attack(closest_elf_to_elf)
        else:
            elf.move_to(closest_elf_to_elf)
    elif elf.in_attack_range(target):
        elf.attack(target)
    elif building is None:
        if len(game.get_my_mana_fountains())<constants.MANA_FOUNTAINS:
            if elf.can_build_mana_fountain():
                elf.build_mana_fountain()
            else:
                elf.move_to(target)
        else:
            if elf.can_build_portal():
                elf.build_portal()
            else:
                elf.move_to(target)
        building = elf
    else:
        elf.move_to(target)
# }

def process_portals(game):
    """
        Processes the portals: finds the closest one to the castle and makes it spawn lava giants. if there's an elf near a portal that portal should spam ice trolls

        game - The game instance
    """

    closest_to_enemy_castle = None
    for p in game.get_my_portals():
        ice_trolls = False
        for e in game.get_enemy_living_elves():
            if e.distance(p) < constants.CLOSE_ENEMY_ELF_TO_PORTAL_RANGE:
                ice_trolls = True

        if ice_trolls:
            if p.can_summon_ice_troll():
                p.summon_ice_troll()

        dst = p.distance(game.get_enemy_castle())
        if not ice_trolls and dst < game.get_my_castle().distance(game.get_enemy_castle()) / 2 and (closest_to_enemy_castle is None or closest_to_enemy_castle.distance(game.get_enemy_castle()) > dst):
            closest_to_enemy_castle = p

    if closest_to_enemy_castle is not None:
        if closest_to_enemy_castle.can_summon_lava_giant():
            closest_to_enemy_castle.summon_lava_giant()
