╔╗ ╔╗       ╔═╗                            ╔╗                         ╔╗  
║║ ║║       ║╔╝                           ╔╝╚╗                        ║║  
║║ ║║╔═╗ ╔╗╔╝╚╗╔══╗╔═╗╔╗╔╗    ╔══╗╔══╗╔══╗╚╗╔╝    ╔══╗╔══╗╔══╗ ╔═╗╔══╗║╚═╗
║║ ║║║╔╗╗╠╣╚╗╔╝║╔╗║║╔╝║╚╝║    ║╔═╝║╔╗║║══╣ ║║     ║══╣║╔╗║╚ ╗║ ║╔╝║╔═╝║╔╗║
║╚═╝║║║║║║║ ║║ ║╚╝║║║ ║║║║    ║╚═╗║╚╝║╠══║ ║╚╗    ╠══║║║═╣║╚╝╚╗║║ ║╚═╗║║║║
╚═══╝╚╝╚╝╚╝ ╚╝ ╚══╝╚╝ ╚╩╩╝    ╚══╝╚══╝╚══╝ ╚═╝    ╚══╝╚══╝╚═══╝╚╝ ╚══╝╚╝╚╝
                            _                    _ 
                          ( )                 /  )
  ___ ___    __   ___ ___ | |_     __  _ __  (_  |
/  _   _  \/ __ \  _   _  \  _ \ / __ \  __)   | |
| ( ) ( ) |  ___/ ( ) ( ) | |_) )  ___/ |      | |
(_) (_) (_)\____)_) (_) (_)_ __/ \____)_)      (_)
                                                  
## Forest Navigation with Animal Avoidance:

This program simulates a forest navigation scenario where a person must navigate through a forest filled with animals and obstacles to reach a treasure. It utilizes uniform cost search to find the optimal path while considering various factors such as obstacles, animals, and the cost associated with traversing different types of cells.

### Table of Contents:

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Explanation of Code](#explanation-of-code)

### Introduction:

In this program, the user defines the size of the forest grid, and the program randomly generates a grid layout with animals, obstacles, and a start (Northwest corner) and endpoint (Southeast corner). The person navigates from the start to the endpoint while avoiding animals and obstacles. Uniform cost search algorithm is used to find the optimal path considering the varying costs associated with different cells.

### Features:

- Dynamic generation of forest grid with random placement of animals, obstacles, and endpoints.
- Calculation of costs associated with different types of cells (safe cells, obstacles, and animals).
- Utilization of uniform cost search algorithm to find the optimal path from the start to the endpoint.
- Consideration of probabilities for encountering animals and determining whether the person gets killed or not.

### Explanation of Code:

This section provides an overview of the key components and functionalities of the provided code for forest navigation with the A* search algorithm.

- **Grid Generation**: A list of nodes is made. each node consists of random things either can be Animal "A" , obstacle "-" , safe " ", endpoint "|".
- **Cost Assignment**: The loops iterate through each node and check whether if it is obstacle then genarates random cost b/t (-4,-2) , if it is safe then assign random cost b/t (-3,-2), if animal then check considering probabbilities whether person will be kiiled or not. If killed then assign rendom cost b/t (-4,-2) and if not then (-3,-2)
- **Uniform cost search Algorithm**:  After formation of grid we apply priority qeue operation on grid directly beacuase it includes symbols and cost as well. The loop breaks when goal node is reached.
- **Two step backward**: Every time when it faces endpoint goes two node back from where it comes from


### Requirements
- Python 3.x
- No external dependencies are required.

### Usage

1. Clone the repository or download the provided code.
2. Ensure you have Python installed on your system.
3. Run the program in your preferred Python environment.
4. Follow the instructions to input the number of rows and columns for the forest grid.
5. The program will generate a grid layout and display the optimal path from the start to the endpoint along with the total cost.

Example command to run the program:
```bash
python forest_navigation.py

