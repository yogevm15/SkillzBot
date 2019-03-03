from elf_kingdom import *



def init(game):
    global enemyPortals, enemyElves, enemyCastle, enemyIceTrolls, enemyLavaGiants, enemyManaFountains, myCastle, myPortals, myManaFountains, myElves, myIceTrolls
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
