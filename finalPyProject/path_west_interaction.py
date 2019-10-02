from adventurelib import *
from porch import *
import time

@when('use key on gate')
@when('use key in gate')
@when('unlock gate with key')
@when('open gate with key')
def unlock_gate():
    item_in_inventory = inventory.take('key')
    if not item_in_inventory:
        print("You need the key!")
    else:
        say(f"You unlock the gate")
        time.sleep(1)
        say("""
            The doors swing open! You have made it! From here you can escape
            this evil place and look forward to playing much better games on
            your own free time. Rejoice! This is a victory for us all!
            """)
        time.sleep(1)
        exit()
