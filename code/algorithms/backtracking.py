

def backtrace(dictionary, solution_state): 
    lol = []
    
    while dictionary[solution_state] != None:

        solution_state = dictionary[solution_state]

        lol.append(solution_state)
    
    print(len(lol))
    return lol