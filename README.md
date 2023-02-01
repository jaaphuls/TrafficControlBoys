# Rush hour project

This project consist of solving various Rush Hour puzzels. There are 2 types of cars, there are cars that cover two spaces on the board and there are trucks that cover 3 spaces on the board. The puzzle is solved when the red car is moved out the exit in the board by shifting the cars and truck out of the path of the red car. It is not possible to move one car over the other car or pick it up. It is really hard to decide if one move is helpfull to do or if it just makes it worse. All of the results we collected are listed in the results folder and some insights are given in the [results README](https://github.com/jaaphuls/TrafficControlBoys/blob/main/code/results/README.md). The goal is to create an algorithm that solves the puzzels in as few steps as possible as displayed in the image below.

![RushHour2](https://user-images.githubusercontent.com/98396172/211304990-5ac416e4-6c5f-41ac-90bc-79ca68478e87.jpeg)


## - Requirements

This codebase is written entirely in Python 3.9.13
requirements.txt contains all the packages needed to succesfully run the file. 
To install these packages use the following code: 

``` pip install -r requirements.txt ```


## - Usage

An example can be run by calling:

``` python main.py ```

The user is subsequently asked for a few prompts: 

``` 
What are the board dimensions (6x6, 9x9 or 12x12)?
```

``` 
Which game would you like to play?

Enter game number:
```

``` 
Which algorithm would you like to use? 

1. random

2. breadth first search

3. beam search 
```

The scirpt will run the chosen algorithm on the chosen game and output the file in the [results](https://github.com/jaaphuls/TrafficControlBoys/tree/main/code/results) folder


## - Structure

The following list describes the most important folders and files in the project, and where to find them:

- **/code**: contains all the code of this project
  - **/code/algorithms**: contains the code for the algorithms
  - **/code/classes**: contains the code for the classes of this case
  - **/code/results**: contains all the results of the various algorithms
  - **/code/visualisation**: contains the code for the visualization
- **/data**: contains the various data files needed to create and visualize the board
- **/docs**: contains the UML diagram of the code
- **/.gitignore**: specifies intentionally untracked files that Git should ignore
- **/README.md**: contains the readme file that is shown on the main page of the repository (the file you are currently reading)
- **/main.py**: this is the main python file in which all the needed files are called and output is created
- **/requirements.txt**: contains all the packages that need to be installed to run the script

## - Algorithms & heurstics

Hier een stukje schrijven over elk algoritme: 

- **Random** 
*Our random algorithm is given a start state and from this start state checks for every possible next-state. it picks one of these next-stape and considers that a step in the game. Our algorithm has no added constraints next to the rules of the game rush-hour, thus it can revisit previous states. The algorithm repeats this process untill a solution is found.*

- **Breadth first search**
*Our breadth-first algorithm is given a mother state and finds all possible child states. it then goes over these child states and considers them the new mother states and finds their child states. Each time it does this it is considered a move or step. it repeats this process untill a child state is the solution. Once the solution is found we use a backtrace function that finds the direct pass from the first mother state to the final child state.*

- **Beam search**
*Our beam search heuristic is applied to our breadth-first algorithm in the bigger board sizes (9x9, 12x12). Instead of going through all the possible child states it randomly selects an x amount of child states to continue breadth-first on untill it finds the solution. This is because the state-space of these board is so large, which means it would take too long for our breadth-first algorithm to finish these boards.*


## - Objective function

Try to minimalise the amount of steps that it takes to solve the puzzle

Think about constraits; no negative amount of steps, no jumping of cars etc. 

## - State-space

To better understand the case and to have an idea of the scale of the problem, it may be a good idea to get an estimation of the size of the state space of the case.
The state space is the total number of valid states that are possible in the case. In our case, the number of possible positions that the vehicles can have on the board. \
To calculate this number, it must first be clear which general formula should be used. There are four possible formulas, which are listed below. Which formula is applicable in our case depends on two questions:

1. Does the order matter?
2. Can the same possibilities be repeated?

![State-space formulas](https://user-images.githubusercontent.com/117074945/216120687-4053e0e8-6c7a-4aa4-b5cd-e942caf0519f.png)

In our case, "Order" actually means the positions on the game board. These properties are of course important, so the first answer is "Yes". The second question seems a bit more difficult to answer, but for us, this question actually means: "Are vehicles allowed to have been in the same place?"\
The answer to the second question is therefore also a "Yes", because when a parking space is available, a car may be moved there, even if this space has been occupied before.

This together means that the general formula to be used is:  ${n}^{r}$.\
In this formula, $n$ would correspond to the number of choices a vehicle can make. In other words: the number of positions it can be moved to. This number is raised to the exponent $r$, which corresponds to the total amount of vehicles that could make a move.

The number of possible moves always depends on the current game board position, which is constantly changing. This makes it difficult to exactly calculate the total state space in this case, which is why we need a simplification:\
Now let's imagine that vehicles can drive over each other, stand on top of each other and thus no longer obstruct each other's way. Although this is just one simplification, the amount of possible moves will now only be determined by the start positions and will not change together with the board.\
This simplification can lead to a larger state space, but it is easier to calculate and gives a good estimation of how the board size and especially the number of vehicles drastically increase the state space.

Because the number of moves a vehicle can make on a free board of width $N$ is equal to $N - 1$ for a car and $N-2$ for a truck, the state space formula would then be:
$$state \ space={\left( width - 1 \right)}^{number of cars}\cdot {\left( width - 2 \right)}^{number\ of\ trucks}$$
## Auteurs
- David van Hulst
- Jaap Hulsbosch
- Samuel Rose
- Florian Ketelaar
