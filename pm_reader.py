import pandas as pd
filepath = r'C:\Users\kingj\Documents\My Games\Pokemon Showdown\Logs\2021-05\pm-csc2405jbm.txt'
substring = 'csc2405_jbm: !data '
intab = ''
outtab = ''

with open(filepath) as f:
    lines = f.readlines()
stack = []


i = 0
for line in lines:
    stack.append(line)
    i = i + 1
df = pd.Series(stack)

for line in df:
    if substring in line:
        stack.append(line)

def smartshell2():
    for line in stack:
        pmons = list(map(lambda x: x.replace('csc2405_jbm:', '').replace('!data','').replace('\n',''), pmons))
    pmons = [e[11:] for e in pmons]
    print(pmons)

def smartshell():
    for line in mons:
        xmons = list(map(lambda x: x.replace('csc2405_jbm:', '').replace('!data','').replace('\n',''), xmons))
    xmons = [e[11:] for e in mons]
    return xmons
print(smartshell())






    

    


