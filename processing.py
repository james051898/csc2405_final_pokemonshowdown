# source: https://www.kaggle.com/fruityfritz/pre-processing-showdown-moveset-text-files
# This code is excellent and efficiently aggregates usage data

def get_index_positions(list_of_elems, element):
    '''
    Returns the indexes of all occurrences of give element in the given list
    '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

def process_showdown_moveset_data(filename="gen8ou-1825.txt"):
    """
    Processes Smogon moveset data and returns it in a dictionary per Pokemon
    
    Inputs:
    - filepath: string of the filepath
    - filename: string of the filename WITHOUT the file extension
    
    Returns dictionary of information indexed by Pokemon
    """
    # importing each line of data to be parseda
    with open(filename) as f:
        lines = f.readlines()
    # splitting the lines of data per each Pokemon
    lines_per_pokemon = [] # list of lists of lines pertaining to each Pokemon
    beginning_line = 0 # initializing
    for line_no in range(len(lines)-1):
        # looking for lines with repeating beginning to the line indicating the end and start of a new Pokemon data stream
        if lines[line_no][:3] == " +-" and lines[line_no+1][:3] == " +-":
            lines_per_pokemon.append(lines[beginning_line:line_no+1])
            beginning_line = line_no+1
    
    # Looping through each Pokemons alotted lines and extracting the information
    data = {} # dictionary to store the Pokemon information
    for info in lines_per_pokemon:
        # pre-allocating the per Pokemon dictionary
        d = {"usage":[],"abilities":[],"items":[],"spreads":[],"moves":[],"teammates":[]}
        # calling helper function to indentify where the headers for the keys of the dictionary will be
        indices = get_index_positions(info," +----------------------------------------+ \n")
        # stripping the data that will be consistently in the same place
        name = info[1].split(" |")[1].strip() # name of Pokemon
        usage = int(info[3].split(" |")[1].split(": ")[-1]) # number of times used that month
        d["usage"] = usage
        # removing indices for the name, usage, and counters and checks information blocks
        reduced_indices = indices[2:-1]
        # looping through the indices and grabbing the information from each block
        for j, index in enumerate(reduced_indices):
            var = info[index+1].split(" |")[1].strip() # variable name
            if var != "Checks and Counters": # easier just to check for this
                # Grabbing the individual data from the block by looking between the indices
                   for line in info[index+2:reduced_indices[j+1]]:
                    # splitting the information into the string and the percentage
                    tokens = line.split(" |")[1].strip().split(" ")
                    # some strings are multiple words, looping through all but the last split and concatenating back
                    s = "" 
                    for token in tokens[:-1]:
                        s += token + " "
                    # adding just the float of the percentage
                    percentage = float(tokens[-1].split("%")[0])
                    # appending the list to the dictionary
                    d[var.lower()].append([s.strip(),percentage])

        data[name] = d
        
    return data

