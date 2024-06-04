#                          _                       _   
#  _ __   ___  _ __   ___ | |__  ___  _ _         / |  
# | '  \ / -_)| '  \ / -_)|  _ \/ -_)| '_|        | |  
# |_|_|_|\___||_|_|_|\___||____/\___||_|          |_|  


#                                        ___    _____        
#   _____ _____  _____  _________ __  __| _/ __| _/__| ____  
#  /     \\__  \ \__  \ \___  /  |  \/ __ | / __ ||  |/    \ 
# |  | |  \/ __ \_/ __ \_/   /|  |  / /_/ |/ /_/ ||  |   |  \
# |__|_|  /____  /____  /____ \____/\____ |\____ ||__|___|  /
#       \/     \/     \/     \/          \/     \/        \/ 


#  __  __      __   __   __ 
#   _)  _)o /|  _) (__) (__)
#  /__ /__|  | __) (__) (__)
                          

import random
import heapq
def uniform_cost_search(grid, start, goal):
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)] #possible moves
    priority_qeue = [] #will make prority code for child nodes
    visited = set() #having visted nodes
    parents = {} #accepted paths will be stored
    heapq.heappush(priority_qeue, (0, start))

    while priority_qeue:
        current_cost, current_node = heapq.heappop(priority_qeue) # will pop smallest to explore its child
        
        # Check if current node is the goal
        if current_node == goal:
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start)
            path.reverse()
            total_cost_n = sum(grid[m][n][1] for m,n in path)
            return path , total_cost_n
        
        # Add current node to visited
        visited.add(current_node)
        
        # Explore neighbors
        for move in movements:
            # Caheck its negbor coordinates
            neighbor = (current_node[0] + move[0], current_node[1] + move[1])
            # Check if neighbor is within grid boundaries
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                # Check if neighbor is not an obstacle and not in the closed set
                if grid[neighbor[0]][neighbor[1]][0] != '-' and neighbor not in visited:
                    # Calculate cost for neighbor
                    Path_Cost = current_cost + grid[neighbor[0]][neighbor[1]][1]
                    heapq.heappush(priority_qeue, (Path_Cost, neighbor))
                    parents[neighbor] = current_node
    
    # If goal not found
    return None,None

if __name__ == "__main__":
    rows_input = int(input("enter num of rows : "))
    cols_input = int(input("enter num of col : "))
    grid_auto = []

    #forming grid having animal,endpoints and obstacles in random cells
    # space represent safe cell
    # '-' represent obstacle or cell difficult to treverse
    # 'A' represent animal in a cell
    # '|' represent endpoint

    for i in range(rows_input):
        row = [random.choice([" ", "-", "A","|"]) for j in range(cols_input)]
        grid_auto.append(row)


    probabilities = [0.2,0.8] #probablities of killing and not killing of a person by animal
    #giving cost to cells in a grid representing a forest and its cells having animals, obstacles, endpoint
    for i in range(rows_input):
        for j in range(cols_input):

            #if there is safe cell
            if grid_auto[i][j] == ' ':
                num = random.randint(-3,-1)
                grid_auto[i][j] = [grid_auto[i][j],int(num)]

            #if there is obstacle and difficult to traverse
            elif grid_auto[i][j] == '-':
                num = random.randint(-4,-2)
                grid_auto[i][j] = [grid_auto[i][j],int(num)]

            #if there is endpoint so no any cost but making list in it to balance grid
            elif grid_auto[i][j] == '|':
                grid_auto[i][j] = [grid_auto[i][j],0]

            #if animal occurs in a cell
            elif grid_auto[i][j] == 'A':
                #checking person will be killed or not by considering probabilities
                killed = random.choices([0, 1], weights=probabilities)[0]
                #when a person is saved from animal..... probability = 0.2
                if killed == 0:
                    num = random.randint(-3,-1)
                    grid_auto[i][j] = [grid_auto[i][j],int(num)]
                #when person is killed from animal.... probability = 0.8
                elif killed == 1:
                    num = random.randint(-4,-2)
                    grid_auto[i][j] = [grid_auto[i][j],int(num)]

    
    #placing start at northwest corner and tresure in southest corner
    grid_auto[rows_input-1][0] = ['S',0] # make list to balnce grid as per my logic
    grid_auto[0][cols_input-1] = ['T',0] # make list to balnce grid as per my logic
    for row in grid_auto:
            print(row)
    print("\n----------------------\n")
    path ,total_cost= uniform_cost_search(grid_auto,(rows_input-1,0),(0,cols_input-1))
    print("Path found:", path)
    print("Total cost:", total_cost)
