## Results

In this section the results of our experiments will be shown and evaluated. 

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
| `Game 1 (6x6)` | *6537 steps* | *21 steps* | *27 steps* |
| `Game 2 (6x6)` | *1534 steps* | *15 steps* | *23 steps* |
| `Game 3 (6x6)` | *21735 steps* | *33 steps* | *54 steps* |
| `Game 4 (9x9)` | *16440 steps* | *27 steps* | *44 steps* |
| `Game 5 (9x9)` | *23627 steps* | *no output yet* | *no output yet* |
| `Game 6 (9x9)` | *18582 steps* | *no output yet* | *no output yet* |
| `Game 7 (12x12)` | *38410 steps* | *no output yet* | *no output yet* |
| `Hardest game (6x6)` | *18704 steps* | *49 steps* | *69 steps* |
