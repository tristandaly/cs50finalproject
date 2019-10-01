from adventurelib import *
from inventory import *
import time



porch = Room("""
             The porch looks and feels old. Its wooden structure groans as you
             walk. It smells of old, wet mold. To the SOUTH is the front yard.
             Just NORTH of you is the front door, situated between the left
             window and the right window.
             """)
current_room = porch
set_context('has_door')
