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

Our random algorithm is given a start state and from this start state checks for every possible next-state. it picks one of these next-stape and considers that a step in the game. Our algorithm has no added constraints next to the rules of the game rush-hour, thus it can revisit previous states. The algorithm repeats this process untill a solution is found.

- **Breadth first search**
Our breadth-first algorithm is given a mother state and finds all possible child states. it then goes over these child states and considers them the new mother states and finds their child states. Each time it does this it is considered a move or step. it repeats this process untill a child state is the solution. Once the solution is found we use a backtrace function that finds the direct pass from the first mother state to the final child state.

- **Beam search**
our beam search heuristic is applied to our breadth-first algorithm in the bigger board sizes (9x9, 12x12). Instead of going through all the possible child states it randomly selects an x amount of child states to continue breadth-first on untill it finds the solution. This is because the state-space of these board is so large, which means it would take too long for our breadth-first algorithm to finish these boards.


## - Objective function

Try to minimalise the amount of steps that it takes to solve the puzzle

Think about constraits; no negative amount of steps, no jumping of cars etc. 

## - Statespace

Order = does order matter?
Repetition = can I repeat same possibilitiy?
r = number of options
n = possibilities per option

                        Repetiton
                yes             No
        Yes     n^r             n! / (n-r)!
ORDER 
        No      (r+n -1)! /     n! /
                r!(n-1)!        r!(n-r)!
                

## Auteurs
- David van Hulst
- Jaap Hulsbosch
- Samuel Rose
- Florian Ketelaar
