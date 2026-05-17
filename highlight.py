
from random import choice
from pyscript import document

memories = [
    "The Intramurals brought grea teamwork and fun memories!", 
    "The Food Fair made everyone tired but excited to see what was ahead!",
    "CAT Graduation felt like a huge achievement and made the teachers feel proud!",
    " The Sabayang Pagbigkas showed teamwork and confidence especially during the hours of overtime after tiring classes!"
]

def show_memory(event):
    random_memory = choice(memories)
    document.getElementById(
        "memoryOutput"
    ).innerHTML = random_memory
    