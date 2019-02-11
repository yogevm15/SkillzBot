from elf_kingdom import *

ElfAct = None
enemyPortals = None
enemyElves = None
enemyCastle = None
enemyIceTroll = None
enemyLavaGiant = None
myPortals = None
myCastle = None
myElves = None
myIceTroll = None
closestEnemyToEvase = None
closestEnemyToCastle = None
closestEnemyToElfInDefendRange = None
closestPortalToElf = None
isSummonIceNeeded = None
isBuildingNeeded = None

#Initialize
def init(game):
    enemyPortals = game.get_enemy_portals()
    enemyElves = game.get_enemy_living_elves()
    enemyCastle = game.get_enemy_castle()
    enemyIceTroll = game.get_enemy_ice_trolls()
    enemyLavaGiant = game.get_enemy_lava_giants()
    enemyManaFountains = game.get_enemy_mana_fountains()
    myCastle = game.get_my_castle()
    myPortals = game.get_my_portals()
    myManaFountains = game.get_my_mana_fountains()
    myElves = game.get_my_living_elves()
    myIceTroll = game.get_my_ice_trolls()


def do_turn(game):
    if game.turn == 1:
        init(game)
    handle_act(game)
    #ManaClass.HandleMana(game);
    pass

def handle_act(game):
    counter = 0
    for p in myPortals:
        if p.distance(enemyCastle) < constants.SUMMON_LAVA_GIANT_RANGE_FROM_CASTLE + 100:
            counter += 1

    if counter > 1:
        game.debug("We Have At Least Two Agressive Portals, Elves Attacking Agressive")
        ElfAct = 2
        return
