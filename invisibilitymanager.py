from elf_kingdom import *
import Default_Values
import constants


def check_invisibility(game,elf):
    if len(elf.current_spells)>0:
        spell = elf.current_spells[0]
        if elf.can_cast_speed_up() and spell.expiration_turns <2:
            for e in Default_Values.enemyElves:
                if e.distance(elf)<750:
                    return True
            for i in Default_Values.enemyIceTrolls:
                if i.distance(elf)<750:
                    return True
    elif elf.can_cast_speed_up():
        for e in Default_Values.enemyElves:
            if e.distance(elf)<750:
                return True
        for i in Default_Values.enemyIceTrolls:
            if i.distance(elf)<750:
                return True
    return False