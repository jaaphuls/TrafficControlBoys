## Results

In this section the results of our experiments will be shown and evaluated. 


The GIF below visualises the breadth first search algorithm on game 2


![GIF Rush Hour](https://github.com/jaaphuls/TrafficControlBoys/blob/main/data/gif_rh_AdobeExpress.gif)

## - Structure

The folder is divided into three subfolders: 
  - **breadth_first_search**: contains the results from the breadth first search algorithm
  - **random_beam_search**: contains the results from the random beam search algorithm
  - **random_results**: contains the results from the random algorithm

Every subfolder contains a csv file cointaining the moves -- ([example](https://github.com/jaaphuls/TrafficControlBoys/blob/main/code/results/breadth_first_search/6x6_1_bfs.csv)) 

It also contains a txt file with the terminal output of the game and algorithm -- ([example](https://github.com/jaaphuls/TrafficControlBoys/blob/main/code/results/breadth_first_search/6x6_1_terminal_output_bfs.txt))

## - Tables

*This table shows the steps required to reach the solution (random algorithm displays the mean of 1000 iterations)*
|     | `Random algorithm` | `Breadth first search algorithm` | `Random beam search algorithm` |
| --- | --- | --- | --- |
| `Game 1 (6x6)` | *6500 steps* | *21 steps* | *27 steps* |
| `Game 2 (6x6)` | *1500 steps* | *15 steps* | *23 steps* |
| `Game 3 (6x6)` | *21000 steps* | *33 steps* | *54 steps* |
| `Game 4 (9x9)` | *16000 steps* | *27 steps* | *44 steps* |
| `Game 5 (9x9)` | *23000 steps* | *no output yet* | *35 steps* |
| `Game 6 (9x9)` | *18000 steps* | *no output yet* | *52 steps* |
| `Game 7 (12x12)` | *38000 steps* | *no output yet* | *no output yet* |
| `Hardest game (6x6)` | *18000 steps* | *49 steps* | *69 steps* |

*The next table shows the time required to reach the solution (random algorithm displays the mean of 1000 iterations)*
|     | `Random algorithm` | `Breadth first search algorithm` | `Random beam search algorithm` |
| --- | --- | --- | --- |
| `Game 1 (6x6)` | *0.13 seconds* | *0.34 seconds* | *0.30 seconds* |
| `Game 2 (6x6)` | *0.04 seconds* | *1.99 seconds* | *1.88 seconds* |
| `Game 3 (6x6)` | *0.50 seconds* | *6.67 seconds* | *5.15 seconds* |
| `Game 4 (9x9)` | *0.78 seconds* | *527 seconds* | *409 seconds* |
| `Game 5 (9x9)` | *1.04 seconds* | *no output yet* | *12 hours* |
| `Game 6 (9x9)` | *1.03 seconds* | *no output yet* | *10.5 hours* |
| `Game 7 (12x12)` | *4.19 seconds* | *no output yet* | *no output yet* |
| `Hardest game (6x6)` | *0.49 seconds* | *13.94 seconds* | *11.38 seconds* |

## - Histograms

Three histograms of the random distributions (the others can be found [here](https://github.com/jaaphuls/TrafficControlBoys/tree/main/code/results/random_results/random_algorithm)): 

Game 1: 

![game1](https://github.com/jaaphuls/TrafficControlBoys/blob/main/code/results/random_results/random_algorithm/2_step/results_steps_game_2_2_steps.png) 


Game 5: 

![game5](https://github.com/jaaphuls/TrafficControlBoys/blob/main/code/results/random_results/random_algorithm/2_step/results_steps_game_5_2_steps.png)

Game 8 (hardest game): 

![game8](https://github.com/jaaphuls/TrafficControlBoys/blob/main/code/results/random_results/random_algorithm/2_step/results_steps_game_8_2_steps.png)

## - Evaluation

While running the various algorithms we created, there were a few remarkable things to observe. Although the random algorithm did yield the greatest number of moves, it always took the least amount of time to run. Also, this algorithm was able to find a solution, which did not always seem to be the case for the other algorithms. The runtime could vary greatly, so we ran it 1000 times to get a better idea of how fast it could solve the Rush Hour puzzles. Even after so many runs, the minimum number of moves before the random algorithm was finished was still very large.\
The Breadth first search algorithm could always find the optimal solution, if only it could run long enough. But this is where things could go wrong with the larger boards, as the state space of a 12x12 board could be more than the squared state space of the 9x9 boards! This resulted in a very long runtime for the 12x12 boards, and also for the 9x9 boards with more vehicles on it. That is why we did not have enough time to find the optimal solution for some of the 9x9 boards, nor the 12x12 one.\
The Random beam search algorithm, however, could take a shorter time to find a decent solution, although not the best one possible. It was also not always able to even find a solution, as it could end up in a dead end. As the algorithm could go deeper in the solution tree in less time, it was able to find solutions for the bigger 9x9 boards. So although this algorithm did not always resulted in the best solutions, it could find solutions to the 9x9 boards that the breadth first algorithm could not solve. After all, finding a decent solution (but not the best one) is better than finding no solution at all.
