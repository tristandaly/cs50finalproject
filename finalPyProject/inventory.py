from adventurelib import *
from map import *
from out_front import *
from path_west import *

inventory = Bag()



@when('inventory')
def show_inventory():
    print('You have: ')
    if not inventory:
        print('nothing')
        return
    for item in inventory:
        print(f'* {item}')
