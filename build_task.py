import constants
from elf_kingdom import *
import utils
import math


class BuildTask(object):
    def __init__(self, game, location, type_of_building):
        """

        :param game:
        :param location:
        :param type_of_building:
        :type type_of_building: type
        """
        self.location = location
        self.type_of_building = type_of_building
        self.elf = self.choose_elf(game)

    def choose_elf(self, game):
        """
        Chooses the best elf for a building task by distance
        :param game: The game instance
        :type game: Game
        :return: The closest elf. None if all are dead.
        """
        return utils.sort_by_distance(game.get_my_living_elves(), self.location)[0]

    def process_building(self, game):
        """
        Makes an elf move and build a building
        :return: Whether or not the build task succeeded
        """
        if not self.elf.location.equals(self.location):
            self.elf.move_to(self.location)
            return False
        else:
            if self.type_of_building is ManaFountain:
                self.elf.build_mana_fountain()
            elif self.type_of_building is Portal:
                self.elf.build_portal()
            else:
                raise Exception("Type of building was invalid! type: " + str(self.type_of_building))
        return True


def get_build_task(game):
    """
    Calculates and returns the current build task
    :param game: The game
    :type game: Game
    :return: The build task if one is needed, else False
    """
    castle_loc = game.get_my_castle().get_location()
    mid = game.get_my_castle().get_location().towards(game.get_enemy_castle(), constants.DEFENSE_BUILDINGS_RADIUS)
    game.debug("Mid: " + str(mid))
    locations = []
    need_fountains = utils.need_mana_fountains(game)
    need_portals = utils.need_defense_portals(game) and not need_fountains

    game.debug("Needs: " + str(need_fountains) + "," + str(need_portals))
    for i in range(360):
        ang = float(i) * math.pi / 180
        x = int(math.cos(ang) * constants.DEFENSE_BUILDINGS_RADIUS)
        y = int(math.sin(ang) * constants.DEFENSE_BUILDINGS_RADIUS)
        loc = Location(castle_loc.row + y, castle_loc.col + x)

        if game.can_build_mana_fountain_at(loc) and need_fountains or game.can_build_portal_at(loc) and need_portals:
            locations.append(loc)

    utils.sort_by_distance(locations, mid)
    game.debug("Locations Found: " + str(locations))

    if need_fountains:
        type_of_building = ManaFountain
        location_index = -1
    elif need_portals:
        type_of_building = Portal
        location_index = 0
    else:
        return False
    if len(locations) < 1:
        return False

    return BuildTask(game, locations[location_index], type_of_building)