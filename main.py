import threading
import time as t
import pandas as pd
import logging
import processing as p
import socks as s
import my_team as my
import sys

def smartshell():
    filepath = r'C:\Users\kingj\Documents\My Games\Pokemon Showdown\Logs\2021-05\pm-csc2405jbm.txt' # file from pokemon showdown chat logs
    filepath2 = r'gen8ou-1825.txt' # usage data
    substring = 'csc2405_jbm: !data '# substring information to be deleted
    
    with open(filepath) as f:
        lines = f.readlines()
    
    stack = []
    mons = []
    oppmoves = []

    for line in lines:
        stack.append(line) # I used a stack because it is more seamless to input into a dataframe
        
    df = pd.Series(stack)
    for line in df:
        if substring in line:
            mons.append(line)# adds the pokemon name into the stack
            
    for line in mons:
        mons = list(map(lambda x: x.replace('csc2405_jbm:', '').replace('!data','').replace('\n',''), mons))
    mons = [e[11:] for e in mons]# this code removes white space from pokemon names so they can be compared
    
    data = p.process_showdown_moveset_data(filepath2)# uses program from kaggle to neatly aggregage usage statistics
    
    percent = []
    i = 0
    while i < 6:
        oppmoves = []
        mon = str(mons[i])
        for moves, percent in data[mon]["moves"]:
            oppmoves.append(moves)
            print(f"{mon}: {oppmoves.pop()}/{percent}%") # this code is used to iterate through usage statistics and print to text file
        i = i + 1

def smartshell2(): # this code is the same as above, however, it creates a dataframe instead of printing

    filepath = r'C:\Users\kingj\Documents\My Games\Pokemon Showdown\Logs\2021-05\pm-csc2405jbm.txt'
    filepath2 = r'gen8ou-1825.txt'
    substring = 'csc2405_jbm: !data '
    with open(filepath) as f:
        lines = f.readlines()
    xstack = []
    xmons = []
    xoppmoves = []

    for line in lines:
        xstack.append(line)
    df = pd.Series(xstack)
    for line in df:
        if substring in line:
            xmons.append(line)
            
    for line in xmons:
        xmons = list(map(lambda x: x.replace('csc2405_jbm:', '').replace('!data','').replace('\n',''), xmons))
    xmons = [e[11:] for e in xmons]
    
    data = p.process_showdown_moveset_data(filepath2)
    opponent_frame = pd.DataFrame()
    print(xmons)
        
def main(): 
    sys.stdout = open("opponents.txt", "w")   
    thj = threading.Thread(target = smartshell2())
    thj.start()
    thj.join()
    sys.stdout.close() # thread to write opponents pokemon to text file
    
    sys.stdout = open("text.txt", "w") # the following threads write to my own text file
    
    
    th1 = threading.Thread(target=smartshell())
    th1.start()
    
    th1.join()
    # thread two-seven
    print("\n")
    
    th2 = threading.Thread(target =s.dmgcalc())
    th2.start()
    
    th2.join()

    print("\n")        
    th3 = threading.Thread(target = my.print1())# the following code is in lists, however, I have implemented a dataframe that is more organized
    th3.start()
    
    th3.join()
    
    th4 = threading.Thread(target = my.print2())
    th4.start()
    
    th4.join()
    
    th5 = threading.Thread(target = my.print3())
    th5.start()
    
    th5.join()
    
    th6 = threading.Thread(target = my.print4())
    th6.start()
    
    th6.join()
    
    th7 = threading.Thread(target = my.print5())
    th7.start()
    
    th7.join()
    
    th8 = threading.Thread(target = my.print6())
    th8.start()
    
    th8.join()
    


    sys.stdout.close()
if __name__ == '__main__':
    main()


