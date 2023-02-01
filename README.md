# Rush hour project

This project consist of solving various Rush Hour puzzels. There are 2 types of cars, there are cars that cover two spaces on the board and there are trucks that cover 3 spaces on the board. The puzzle is solved when the red car is moved out the exit in the board by shifting the cars and truck out of the path of the red car. It is not possible to move one car over the other car or pick it up. It is really hard to decide if one move is helpfull to do or if it just makes it worse. The goal is to create an algorithm that solves the puzzels in as few steps as possible as displayed in the image below.


![RushHour2](https://user-images.githubusercontent.com/98396172/211304990-5ac416e4-6c5f-41ac-90bc-79ca68478e87.jpeg)

## - Requirements

This codebase is written entirely in Python 3.9.13

## - Usage

An example can be run by calling:

``` python main.py ```

The user is subsequently asked for a few prompts: 

``` What are the board dimensions (6x6, 9x9 or 12x12)? ```

``` Which game would you like to play?```

``` Enter game number: ``` 

``` Which algorithm would you like to use?  ```

``` 1. random ```

``` 2. breadth first search ```

``` 3. beam search ```



## - Structure

The following list describes the most important folders and files in the project, and where to find them:

- **/code**: contains all the code of this project
  - **/code/algorithms**: contains the code for the algorithms
  - **/code/classes**: contains the code for the classes of this case
  - **/code/visualisation**: contains the code for the visualization
- **/data**: contains the various data files needed to create and visualize the board

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
