from elf_kingdom import *
from Default_Values import *
import constants

class ManaReport(object):
    def __init__(self, is_lava_needed, is_ice_needed, is_portal_needed, is_mana_fountain_needed):
        self.is_lava_needed = is_lava_needed
        self.is_ice_needed = is_ice_needed
        self.is_portal_needed = is_portal_needed
        self.is_mana_fountain_needed = is_mana_fountain_needed

# Returns ManaReport
def handle_mana(game, elf_act):
    pass
