from elf_kingdom import *
import Default_Values
import constants
import aggresive_building_act as radius

class ManaReport(object):
    def __init__(self, is_lava_needed, is_ice_needed, is_portal_needed, is_mana_fountain_needed):
        self.is_lava_needed = is_lava_needed
        self.is_ice_needed = is_ice_needed
        self.is_portal_needed = is_portal_needed
        self.is_mana_fountain_needed = is_mana_fountain_needed

# Returns ManaReport
def handle_mana(game, elf_act):
    enemyBuildingFlag = False
    for p in Default_Values.myPortals:
        if p.distance(Default_Values.myCastle)<constants.DEFENSE_PORTAL_RANGE_FROM_MY_CASTLE+500:
            if game.get_my_mana()>190:
                for l in Default_Values.enemyLavaGiants:
                    if l.distance(p) < constants.SUMMON_ICE_TROLL_TO_KILL_ELF_RANGE_FROM_ENEMY_ELF:
                        if p.can_summon_ice_troll():
                            p.summon_ice_troll()
                for e in Default_Values.enemyElves:
                    if e.distance(p) < constants.SUMMON_ICE_TROLL_TO_KILL_ELF_RANGE_FROM_ENEMY_ELF:
                        if p.can_summon_ice_troll():
                            p.summon_ice_troll()
        elif p.distance(Default_Values.myCastle)>2000:
            for e in Default_Values.enemyElves:
                if e.distance(p) < 1500:
                    if p.can_summon_ice_troll():
                        print "summon ice"
                        p.summon_ice_troll()
            if p.can_summon_lava_giant():
                p.summon_lava_giant()
            
