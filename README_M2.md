
 ▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄   ▄▄ 
█       █     █       █       █       █   ▄  █ █       █  █ █  █
█   ▄   █     █  ▄▄▄▄▄█    ▄▄▄█   ▄   █  █ █ █ █       █  █▄█  █
█  █▄█  █     █ █▄▄▄▄▄█   █▄▄▄█  █▄█  █   █▄▄█▄█     ▄▄█       █
█       █     █▄▄▄▄▄  █    ▄▄▄█       █    ▄▄  █    █  █   ▄   █
█   ▄   █      ▄▄▄▄▄█ █   █▄▄▄█   ▄   █   █  █ █    █▄▄█  █ █  █
█▄▄█ █▄▄█     █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█
                           _                    __   
                          ( )                 / __ \ 
  ___ ___    __   ___ ___ | |_     __  _ __  (_)  ) )
/  _   _  \/ __ \  _   _  \  _ \ / __ \  __)    /  / 
| ( ) ( ) |  ___/ ( ) ( ) | |_) )  ___/ |     /  /( )
(_) (_) (_)\____)_) (_) (_)_ __/ \____)_)    (_____/ 
                                                     
                                                     
# Forest Navigation with A* Search:

This program simulates forest navigation using the A* search algorithm. The objective is for a person to navigate through a forest grid, avoiding obstacles and animals, to reach the treasure endpoint.

## Table of Contents:

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Explanation of Code](#explanation-of-code)

## Introduction:

The program generates a forest grid with random placements of obstacles, animals, and endpoints. It then employs the A* search algorithm to find the optimal path from the starting point (northwest corner) to the treasure (southeast corner), considering varying costs associated with different cells and heuristic estimates.

## Features:

- Dynamic generation of forest grid with random obstacle and animal placements.
- Utilization of the A* search algorithm for optimal pathfinding.
- Incorporation of heuristic estimates to guide search towards the goal efficiently.
- Displaying the best path found from start to endpoint.

### Explanation of Code:

This section provides an overview of the key components and functionalities of the provided code for forest navigation with the A* search algorithm.

- **Grid Generation**: A list of nodes is made. each node consists of random things either can be Animal "A" , obstacle "-" , safe " ", endpoint "|".
- **Cost Assignment**: The loops iterate through each node and check whether if it is obstacle then genarates random cost b/t (-4,-2) , if it is safe then assign random cost b/t (-3,-2), if animal then check considering probabbilities whether person will be kiiled or not. If killed then assign rendom cost b/t (-4,-2) and if not then (-3,-2).
- **Heuristic Calculation**: First we find heuristic values for each node from goal node using *manhatan distance*. And append these heuristic values to the node(list). 
- **A* Search Algorithm**: And then apply A* search on the grid diractly because each node contains its heuristic value and the time of applying search no need to find heuristic search.
- **Two step backward**: Every time when it faces endpoint goes two node back from where it comes from.

## Requirements:

- Python 3.x
- No external dependencies required.

## Usage:

1. Clone the repository or download the provided code.
2. Ensure you have Python installed on your system.
3. Run the program in your preferred Python environment.
4. Input the number of rows and columns for the forest grid.
5. The program will generate the forest grid, execute the A* search algorithm, and display the best path found.

Example command to run the program:
```bash
python forest_navigation_astar.py
