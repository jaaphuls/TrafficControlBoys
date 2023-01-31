def backtrace(dictionary, solution_state): 
    lol = [solution_state]
    
    while dictionary[solution_state] != None:

        solution_state = dictionary[solution_state]
        lol.append(solution_state)
    
    return lol