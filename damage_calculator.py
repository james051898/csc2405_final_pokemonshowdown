import pandas as pd

df = pd.read_excel(r'moves.xlsx', index_col = 0)
df2 = pd.read_excel(r'dex.xlsx', index_col = 0)
typechart = pd.read_excel(r'typechart.xlsx', index_col = 0)
spreads = pd.read_excel(r'calc.xlsx', index_col = 0)
opppoke = pd.read_excel(r'opponent_team.xlsx', index_col = 0) # file setup

level = 100.00
ev = 252.00

def findpower(move):
    return df.loc[move, 'power'] # iterates through the moves.xlsx file to get base power

def findmovetype(move):
    return df.loc[move, 'type'] # iterates through the moves.xlsx file to get type

def findcategory(move):
    return df.loc[move, 'category'] # iterates through the moves.xlsx file to get move category

def findtype1(usermon):
    return df2.loc[usermon, 'type_1'] # getter for primary type; iterates through dex.xlsx
    
def findtype2(usermon):
    return df2.loc[usermon, 'type_2'] # getter for secondary type; iterates through dex.xlsx

def isstab(mon, move):
    if findmovetype(move) == findtype2(mon) or findmovetype(move) == findtype1(mon):
        return True
    else:
        return False # Boolean variable to determine stab attack which multiples power by 1.5; iterates through typechart.xlsx

def effectiveness(move, mon):
    if df2.loc[mon, 'type_number'] == 1:
        movetype = findmovetype(move)
        montype = findtype1(mon)
        return typechart.loc[movetype, montype] # Determines effectives type effectiveness of your move
    else:
        movetype = findmovetype(move)
        montype1 = findtype1(mon)
        montype2 = findtype2(mon)
        return typechart.loc[movetype, montype1]*typechart.loc[movetype, montype2]# If pokemon has multiple types, this returns the multiplicative effect
    
def bst(mon):
    hp = df2.loc[mon, 'hp']
    atk = df2.loc[mon, 'attack']
    defense = df2.loc[mon, 'defense']
    spatk = df2.loc[mon, 'sp_attack']
    spdef = df2.loc[mon, 'sp_defense']
    spd = df2.loc[mon, 'speed']
    bstdf = pd.Series([hp, atk, defense, spatk, spdef, spd], index = [1, 2, 3, 4, 5, 6])
    return bstdf # returns a pokemons base stats for later calculations

def max_hp(mon):
    # hp calculation
    lmon = str(mon).lower()
    bstdf = bst(lmon) #HP Base stats
    base = bstdf.iloc[0] # HP is found at the primary index
    return ((base*2.00+31.00+(252/4)+100))+10 # HP calculation seems to be different depending on where you go, I find this to be the most practical
    
def stat_calc(mon, stat): 
    lmon = str(mon).lower()
    bstdf = bst(lmon) 
    return int((int(((2*bstdf.iloc[stat] + 31.00 + int(ev/4)) * level) / 100) + 5))# calculates other stats as they are not unique

def dmgcalc(): # hardcode version for demo
    move = 'fiery dance' # the users move
    oppmon = 'blissey' # the opponents pokemon
    usermon = 'volcarona' # The User's pokemon
    
    # total damage multiplier
    if isstab(usermon, move) == True:
        x = int(1.5)
    else:
        x = int(1.0)
    y = 1.00
    z = 1.00
    y = effectiveness(move, oppmon)
    z = y*x# this is a multiplier that incorporates type multipliers
    # get move power
    
    power = 1.00
    power = findpower(move) # sets the base power for damage calculation
    
    # set up attack & defense
    attack = 1.00
    defense = 1.00
    
    #dmg calculator
    cat = findcategory(move) # A move's category determines whether a pokemon uses sp. attack or attack
    cat2 = cat.replace(' ', '')# removes whitespace
    if cat2 == 'physical': # if physical, uses attack and defence
        attack = stat_calc(usermon, 2)
        defense = stat_calc(oppmon, 3)
    elif cat2 == 'special': # otherwise, calculations use special attack
        attack = stat_calc(usermon, 4)
        defense = stat_calc(oppmon, 5)
    print( f"Volcarona would take out {(z * (attack/defense) * power)/max_hp(oppmon)*100}% of Blissey's health with Fiery Dance") # prints information

def dmgcalc2(move, oppmon, usermon): # this code uses inputs rather than hard code, will need to implement a automated method
    # total damage multiplier
    if isstab(usermon, move) == True:
        x = int(1.5)
    else:
        x = int(1.0)
    y = 1.00
    z = 1.00
    y = effectiveness(move, oppmon)
    z = y*x
    # get move power
    power = 1.00
    power = findpower(move)
    
    # set up attack & defense
    attack = 1.00
    defense = 1.00
    
    #dmg calculator
    cat = findcategory(move)
    cat2 = cat.replace(' ', '')
    if cat2 == 'physical':
        attack = stat_calc(usermon, 2)
        defense = stat_calc(oppmon, 3)
    elif cat2 == 'special':
        attack = stat_calc(usermon, 4)
        defense = stat_calc(oppmon, 5)
    return f"{(z * (attack/defense) * power)/max_hp(oppmon)*100}%" 
     
