def backtrace(dictionary, solution_state): 
    optimal_path = [solution_state]
    
    while dictionary[solution_state] != None:
        solution_state = dictionary[solution_state]
        optimal_path.append(solution_state)
    
    return optimal_path