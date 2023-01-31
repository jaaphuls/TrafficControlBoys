def backtrace(dictionary, solution_state): 
    optimal_path = [solution_state]
    
    while dictionary[solution_state] != None:
        solution_state = dictionary[solution_state]
        optimal_path.append(solution_state)
    
    return optimal_path

def check_50_path(optimal_moves):

    move_list = []
                
    for index3 in range(len(optimal_moves)):

        if index3+1 < len(optimal_moves):

            if optimal_moves[index3+1].string_value != None:
                my_value = optimal_moves[index3].string_value
                my_value2 = optimal_moves[index3+1].string_value

                #print(my_value)

                # Iterate over index
                for element in range(0, len(my_value), 3):
                    car_cord1 = (my_value[element:element+3])
                    car_cord2 = (my_value2[element:element+3])

                    if car_cord1 != car_cord2:
                        if car_cord1[1] != car_cord2[1]:
                            change = int(car_cord2[1]) - int(car_cord1[1])
                            car_cordinates = (car_cord1[0], change)
                            move_list.append(car_cordinates)

                        elif car_cord1[2] != car_cord2[2]:
                            change = int(car_cord2[2]) - int(car_cord1[2])
                            car_cordinates = (car_cord1[0], change)
                            move_list.append(car_cordinates)
        else:
            pass
    
    return move_list