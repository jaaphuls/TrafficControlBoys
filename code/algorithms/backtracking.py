def backtrace(dictionary, solution_state): 
    '''
    Tracks back the solution path of the breadth first search or random beam search algorithm. 
    The function takes a dictionary containing all the moves and the solution state of the board.
    It returns the optimal path the algorithm took to the solution.
    '''

    # Create a list to store the optimal path from initial state to the solution state
    optimal_path = [solution_state]
    
    # Keep looping until the solution state is not None (which means it's the initial state)
    while dictionary[solution_state] != None:

        # Get the previous state from the dictionary using the solution state
        solution_state = dictionary[solution_state]
        # Add the previous state to the optimal path
        optimal_path.append(solution_state)

    return optimal_path



def check_50_path(optimal_moves):
    '''
    Puts together a list with all the moves needed to reach the solution state in a format that check50 can check. 
    The function takes the optimal path to solve the board.
    It returns the a list with all the moves needed to reach the solution state.
    '''

    # Create an empty list to store the moves needed to reach the solution state
    move_list = []
                
    # Iterate through the optimal moves list
    for index in range(len(optimal_moves)):

        # Check if there is a next move in the optimal moves list
        if index+1 < len(optimal_moves):

            # Check if the next move is not None
            if optimal_moves[index+1].string_value != None:
                # Get the string representation of the current and next states
                my_value = optimal_moves[index].string_value
                my_value2 = optimal_moves[index+1].string_value

                # Iterate through the string representation of the current and next states
                for element in range(0, len(my_value), 3):
                    # Get the string representation of the car's position in the current and next states
                    car_cord1 = (my_value[element:element+3])
                    car_cord2 = (my_value2[element:element+3])

                    # Check if the car's position has changed
                    if car_cord1 != car_cord2:
                        # Check if the change is in the y-axis
                        if car_cord1[1] != car_cord2[1]:
                            # Calculate the change in y-axis
                            change = int(car_cord2[1]) - int(car_cord1[1])
                            car_cordinates = (car_cord1[0], change)
                            move_list.append(car_cordinates)

                        # Check if the change is in the x-axis
                        elif car_cord1[2] != car_cord2[2]:
                            # Calculate the change in x-axis
                            change = int(car_cord2[2]) - int(car_cord1[2])
                            car_cordinates = (car_cord1[0], change)
                            move_list.append(car_cordinates)

        else:
            pass
    
    return move_list
