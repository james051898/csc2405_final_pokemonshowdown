import pandas as pd
import numpy as np
import time as t
from openpyxl.utils.cell import col
# The purpose of this program is to upload my team in a neat format to be used for damage calculations

with open(r"C:\Users\kingj\Documents\My Games\Pokemon Showdown\Teams\[gen8ou] team.txt") as f:
    lines = f.readlines()
stack = []
col = []
items = []

i = 0
for line in lines:
    stack.append(line)
    # print(f"{i}: {line}")
    i = i + 1
    
# empty arrays for pokemon dataframe below
poke1 = []
poke2 = []
poke3 = []
poke4 = []
poke5 = []
poke6 = []
temp = ""

for x in range(56):
    if x in (0, 9, 19, 28, 37, 47):
        temp = stack[x]
        split_string = temp.split("@",2)
        substring = split_string[0]
        item = split_string[1]
        col.append(substring)
        items.append(item)
        print(split_string) # gets name of pokemon for dataframe columns

i = 0
while i <= 8:
    temp = stack.pop() # each while loop represents a pokemon on my team
    poke1.append(temp)
    i = i + 1
    
while i <= 18:
    temp = stack.pop()
    poke2.append(temp)
    i = i + 1
    
while i <= 27:
    temp = stack.pop()
    poke3.append(temp)
    i = i + 1
    
while i <= 36:
    temp = stack.pop()
    poke4.append(temp)
    i = i + 1

while i <= 46:
    temp = stack.pop()
    poke5.append(temp)
    i = i + 1

while i <= 55:
    temp = stack.pop()
    poke6.append(temp)
    i = i + 1

# reverses fifo ordering
poke1.reverse()
poke2.reverse()
poke3.reverse()
poke4.reverse()
poke5.reverse()
poke6.reverse()

# removes white space
col1 = col.pop().replace(" ", "")
col2 = col.pop().replace(" ", "")
col3 = col.pop().replace(" ", "")
col4 = col.pop().replace(" ", "")
col5 = col.pop().replace(" ", "")
col6 = col.pop().replace(" ", "")

data = {str(col1):[items.pop(), poke1[1], poke1[2], poke1[3], poke1[4:8]],
        str(col2):[items.pop(), poke2[1], poke2[2], poke2[3], poke2[5:9]],
        str(col3):[items.pop(), poke3[1], poke3[2], poke3[3], poke3[4:8]],
        str(col4):[items.pop(), poke4[1], poke4[2], poke4[3], poke4[4:8]],
        str(col5):[items.pop(), poke5[1], poke5[2], poke5[3], poke5[5:9]],
        str(col6):[items.pop(), poke6[1], poke6[2], poke6[3], poke6[4:8]]} 

df = pd.DataFrame(data, columns = [col1, col2, col3, col4, col5, col6], index = ["item", "ability", "spread", "nature", "moves"]) 
# organized dataframe for pokemon
def export_evs(mon):
    return df.loc["spread", mon] # code to export EV spreads
def export_nature(mon):
    return df.loc["nature", mon]# code to export Nature multipliers

    



