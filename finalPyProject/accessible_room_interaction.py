from adventurelib import *
from accessible_room import *
from out_front import *
from porch import *
import time



@when('one')
def first_door():
    say("You open the first door and enter the room.")
    say("Your blood runs cold as you meet your only companion for the rest")
    say("of eternity.")
    time.sleep(2)
    say("""
        "Hullo FelloW!" bellows the rabbit in the top hat. You sit down and watch
        as the magic show begins.
        """)
    time.sleep(2)
    exit()

@when('two')
def second_door():
    say("You open the second door.")
    say("There before you stands a KEY upon a red hill.")
    time.sleep(2)
    say("You take the key.")
    time.sleep(1)
    inventory.add(accessible_room.items.take('key'))
    say("A portal opens to the SOUTH revealing the porch.")


@when('three')
def third_door():
    say("You open the third door.")

@when('four')
def fourth_door():
    say("You open the fourth door.")
