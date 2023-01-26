def backtrace(state_list): 
    moves = {}

    for state in range(len(state_list) - 1):
        
        # get the current and next state 
        current_state = state_list[state]
        next_state = state_list[state + 1]

        # compare the two states to get the moved car 
        original_position = list(set(current_state) - set(next_state))
        print(original_position)
        next_position = list(set(next_state) - set(current_state))
        print(next_position)

        # check in what way the car moves
        if original_position.x < next_position.x: 
            if original_position not in moves: 
                moves[{original_position}] = 1
            else: 
                moves[{original_position}] += 1

        if original_position.x > next_position.x: 
            if original_position not in moves: 
                moves[{original_position}] = 1
            else: 
                moves[{original_position}] -= 1


        if original_position.x > next_position.x: 
            if original_position not in moves: 
                moves[{original_position}] = 1
            else:
                moves[{original_position}] -= 1
        
        if original_position.y < next_position.y: 
            if original_position not in moves: 
                moves[{original_position}] = 1
            else: 
                moves[{original_position}] += 1

    return moves