#                            _                    __   
#                           ( )                 / __ \ 
#   ___ ___    __   ___ ___ | |_     __  _ __  (_)  ) )
# /  _   _  \/ __ \  _   _  \  _ \ / __ \  __)    /  / 
# | ( ) ( ) |  ___/ ( ) ( ) | |_) )  ___/ |     /  /( )
# (_) (_) (_)\____)_) (_) (_)_ __/ \____)_)    (_____/ 
                                                     

#   __    _      __    _          __    __   _   _    
#  / /\  \ \_/  / /\  | |\ |     / /\  ( (` | | | |\/|
# /_/--\  |_|  /_/--\ |_| \|    /_/--\ _)_) |_| |_|  |
                    

#  __  __   __     __   __  
#   _)  _)o  _) /|  _) (__\ 
#  /__ /__| /__  | __)  __/ 
                          

import heapq
import random



# this function find heuristic value using manhattan diatance 
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])



# A* algo
def astar_search(grid, start, goal):
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
                    # Calculate g-score for neighbor
                    g_score = current_cost + grid[neighbor[0]][neighbor[1]][1]
                    # Calculate h-score for neighbor
                    h_score = heuristic(neighbor, goal)
                    # Calculate f-score for neighbor
                    f_score = g_score + h_score
                    
                    heapq.heappush(priority_qeue, (f_score, neighbor))
                    # Update parent node
                    parents[neighbor] = current_node
    
    # If goal not found
    return None,None


if __name__ == "__main__":
    rows = int(input("enter num of rows : "))
    cols = int(input("enter num of col : "))
    # rows = 8
    # cols = 8
    grid = []
    probabilities = [0.2,0.8] #probablities of killing and not killing of a person by animal

    #forming grid having animal,endpoints and obstacles in random cells
    # space represent safe cell
    # '-' represent obstacle or cell difficult to treverse
    # 'A' represent animal in a cell
    # '|' represent endpoint

    for i in range(rows):
        row = [random.choice([" ", "-", "A","|"]) for j in range(cols)]
        grid.append(row)


    #placing start at northwest corner and tresure in southest corner
    grid[rows-1][0] = ['S',0] # make list to balnce grid as per my logic
    grid[0][cols-1] = ['T',0] # make list to balnce grid as per my logic

    #giving cost to cells in a grid representing a forest and its cells having animals, obstacles, endpoint
    for i in range(rows):
        for j in range(cols):


            #if there is safe cell
            if grid[i][j] == ' ':
                num = random.randint(-3,-1)
                grid[i][j] = [grid[i][j],int(num)]

            #if there is obstacle and difficult to traverse
            elif grid[i][j] == '-':
                num = random.randint(-4,-2)
                grid[i][j] = [grid[i][j],int(num)]

            #if there is endpoint so no any cost but making list in it to balance grid
            elif grid[i][j] == '|':
                grid[i][j] = [grid[i][j],0]

            #if animal occurs in a cell
            elif grid[i][j] == 'A':
                #checking person will be killed or not by considering probabilities
                killed = random.choices([0, 1], weights=probabilities)[0]
                #when a person is saved from animal..... probability = 0.2
                if killed == 0:
                    num = random.randint(-3,-1)
                    grid[i][j] = [grid[i][j],int(num)]
                #when person is killed from animal.... probability = 0.8
                elif killed == 1:
                    num = random.randint(-4,-2)
                    grid[i][j] = [grid[i][j],int(num)]


    for row in grid:
            print(row)
    print("\n----------------------\n")

    path , total_cost= astar_search(grid,(rows-1,0),(0,cols-1))
    print("path : ",path,"\n","Total_cost : ",total_cost)


