from adventurelib import *
from characters import *


path_west = Room("""
Brown ground and brown trees about as you make you way through the twisting path.
There are exits to the west and east.
 """)

path_west.items = Bag()

goblin_chef = MaleCharacter('a goblin chef', 'Rather full')
goblin_chef.def_name = 'the goblin chef'
