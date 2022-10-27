

#max volumes of bottles
b1_max = 10
b2_max = 6
b3_max = 5    

start_state = [10,0,0] #initial start state
goal_state = [8,0,0] #final state

queue = [start_state] #initialize queue list and add iniital state to queue
visited = [start_state] #initialize visited list and add iniital state to visited

#output solution
def output(explored, max_queue_length):

    #prints all visited state
    for i in visited:
        print(i[0] , i[1], i[2])
    
    #prints if goal is reached    
    if(i == goal_state):
            print ('\nTime complexity:', str(explored),'nodes explored or popped off the queue.')
            print ('Space complexity:', str(max_queue_length),'nodes in the queue at its max.\n') 

#breadth first search
def bfs():

    explored = 0 #counts number of nodes explored or popped
    max_queue_length = 1 #checks max length of queue
    
    #loop while queue list in not empty
    while(queue):

        current = queue.pop(0) #remove first item from queue and save in variable current
        explored += 1 #adds 1 to nodes explored or popped

        #current water level of bottle b1, b2 and b3
        x = current[0] #b1
        y = current[1] #b2 
        z = current[2] #b3

        #calculated max length of queue
        if len(queue) > max_queue_length:
                max_queue_length = len(queue)

        #check if visited same as goal state
        if(visited[-1] == goal_state):
            output(explored, max_queue_length) 
            return

        #fill b1:10 Liter bottle
        if(x < b1_max and [b1_max, y, z] not in visited):
            visited.append([b1_max, y, z])
            queue.append([b1_max, y, z])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #fill b2:6 Liter bottle
        if(y < b2_max and [x, b2_max, z] not in visited):
            visited.append([x, b2_max, z])
            queue.append([x, b2_max, z])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return
        
        #fill b3:5 Liter bottle
        if(z < b3_max and [x, y, b3_max] not in visited):
            visited.append([x, y, b3_max])
            queue.append([x, y, b3_max])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #empty b1:10 Liter bottle
        if(x > 0 and [0, y, z] not in visited):
            visited.append([0, y, z])
            queue.append([0, y, z])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #empty b2:6 Liter bottle       
        if(y > 0 and [x, 0, z] not in visited):
            visited.append([x, 0, z])
            queue.append([x, 0, z])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #empty b3:5 Liter bottle
        if(z > 0 and [x, y, 0] not in visited):
            visited.append([x, y, 0])
            queue.append([x, y, 0])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b1:10 Liter to b2:6 Liter,    keep remaining in b1:10 Liter       
        if(((x + y) >= b2_max and x > 0) and [x - (b2_max - y), b2_max, z] not in visited):
            visited.append([x - (b2_max - y), b2_max, z])
            queue.append([x - (b2_max - y), b2_max, z])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b1:10 Liter to b3:5 Liter,    keep remaining in b1:10 Liter
        if(((x + z) >= b3_max and x > 0) and [x - (b3_max - z), y, b3_max] not in visited):
            visited.append([x - (b3_max - z), y, b3_max])
            queue.append([x - (b3_max - z), y, b3_max])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b2:6 Liter to b1:10 Liter,    keep remaining in b2:6 Liter
        if(((y + x) >= b1_max and y > 0) and [b1_max, y - (b1_max - x), z] not in visited):
            visited.append([b1_max, y - (b1_max - x), z])
            queue.append([b1_max, y - (b1_max - x), z])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b2:6 Liter to b3:5 Liter,     keep remaining in b2:6 Liter
        if(((y + z) >= b3_max and y > 0) and [x, y - (b3_max - z), b3_max] not in visited):
            visited.append([x, y - (b3_max - z), b3_max])
            queue.append([x, y - (b3_max - z), b3_max])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b3:5 Liter to b1:10 Liter,    keep remaining in b3:5 Liter
        if(((z + x) >= b1_max and z > 0) and [b1_max, y, z - (b1_max - x)] not in visited):
            visited.append([b1_max, y, z - (b1_max - x)])
            queue.append([b1_max, y, z - (b1_max - x)])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b3:5 Liter to b2:6 Liter,     keep remaining in b3:5 Liter
        if(((z + y) >= b2_max and z > 0) and [x, b2_max, z - (b2_max - y)] not in visited):
            visited.append([x, b2_max, z - (b2_max - y)])
            queue.append([x, b2_max, z - (b2_max - y)])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b1:10 Liter to b2:6 Liter,    no left over
        if(((x + y) <= b2_max and x >= 0) and [0, (x + y), z] not in visited):
            visited.append([0, (x + y), z])
            queue.append([0, (x + y), z])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b1:10 Liter to b3:5 Liter,    no left over
        if(((x + z) <= b3_max and x >= 0) and [0, y, (x + z)] not in visited):
            visited.append([0, y, (x + z)])
            queue.append([0, y, (x + z)])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b2:6 Liter to b1:10 Liter,    no left over
        if(((y + x) <= b1_max and y >= 0) and [(x + y), 0, z] not in visited):
            visited.append([(x + y), 0, z])
            queue.append([(x + y), 0, z])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b2:6 Liter to b3:5 Liter,     no left over
        if(((y + z) <= b3_max and y >= 0) and [x, 0, (y + z)] not in visited):
            visited.append([x, 0, (y + z)])
            queue.append([x, 0, (y + z)])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b3:5 Liter to b1:10 Liter,    no left over
        if(((z + x) <= b1_max and z >= 0) and [(x + z) , y, 0] not in visited):
            visited.append([(x + z) , y, 0])
            queue.append([(x + z) , y, 0])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b3:5 Liter to b2:6 Liter,     no left over
        if(((z + y) <= b2_max and z >= 0) and [x, (y + z), 0] not in visited):
            visited.append([x, (y + z), 0])
            queue.append([x, (y + z), 0])
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return                

#depth first search    
def dfs():
    
    explored = 0 #counts number of nodes explored or popped
    max_queue_length = 1 #checks max length of queue
    
    #loop while queue list in not empty
    while(queue):

        current = queue.pop(-1) #remove last item from queue and save in variable current
        explored += 1 #adds 1 to nodes explored or popped

        #current water level of bottle b1, b2 and b3
        x = current[0] #b1
        y = current[1] #b2
        z = current[2] #b3

        #calculated max length of queue
        if len(queue) > max_queue_length:
            max_queue_length = len(queue)

        #check if visited same as goal state
        if(visited[-1] == goal_state):
            output(explored, max_queue_length) 
            return
        
        #empty b1:10 Liter bottle to...
        if(x > 0):
            
            #empty b1:10 Liter bottle
            if([0, y, z] not in visited):
                visited.append([0, y, z])
                queue.append([0, y, z])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return    

            #pour water from b1:10 Liter to b2:6 Liter,    keep remaining in b1:10 Liter  
            if(((x + y) >= b2_max) and [x - (b2_max - y), b2_max, z] not in visited):
                visited.append([x - (b2_max - y), b2_max, z])
                queue.append([x - (b2_max - y), b2_max, z])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

            #pour water from b1:10 Liter to b2:6 Liter,    no left over
            if(((x + y) <= b2_max) and [0, (x + y), z] not in visited):
                visited.append([0, (x + y), z])
                queue.append([0, (x + y), z])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

            #pour water from b1:10 Liter to b3:5 Liter,    keep remaining in b1:10 Liter
            if(((x + z) >= b3_max) and [x - (b3_max - z), y, b3_max] not in visited):
                visited.append([x - (b3_max - z), y, b3_max])
                queue.append([x - (b3_max - z), y, b3_max])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return       

            #pour water from b1:10 Liter to b3:5 Liter,    no left over
            if(((x + z) <= b3_max) and [0, y, (x + z)] not in visited):
                visited.append([0, y, (x + z)])
                queue.append([0, y, (x + z)])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return        
        
        #fill b1:10 Liter bottle
        elif(x < b1_max):
            if([b1_max, y, z] not in visited):
                visited.append([b1_max, y, z])
                queue.append([b1_max, y, z])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

        #empty b2:6 Liter bottle to...
        if(y > 0):
            
            #empty b2:6 Liter bottle       
            if([x, 0, z] not in visited):
                visited.append([x, 0, z])
                queue.append([x, 0, z])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

            #pour water from b2:6 Liter to b1:10 Liter,    keep remaining in b2:6 Liter
            if(((y + x) >= b1_max) and [b1_max, y - (b1_max - x), z] not in visited):
                visited.append([b1_max, y - (b1_max - x), z])
                queue.append([b1_max, y - (b1_max - x), z])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

            #pour water from b2:6 Liter to b1:10 Liter,    no left over
            if(((y + x) <= b1_max) and [(x + y), 0, z] not in visited):
                visited.append([(x + y), 0, z])
                queue.append([(x + y), 0, z])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

            #pour water from b2:6 Liter to b3:5 Liter,     keep remaining in b2:6 Liter
            if(((y + z) >= b3_max) and [x, y - (b3_max - z), b3_max] not in visited):
                visited.append([x, y - (b3_max - z), b3_max])
                queue.append([x, y - (b3_max - z), b3_max])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return
            
            #pour water from b2:6 Liter to b3:5 Liter,     no left over
            if(((y + z) <= b3_max) and [x, 0, (y + z)] not in visited):
                visited.append([x, 0, (y + z)])
                queue.append([x, 0, (y + z)])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return
        
        #fill b2:6 Liter bottle
        elif(y < b2_max):
            if([x, b2_max, z] not in visited):
                visited.append([x, b2_max, z])
                queue.append([x, b2_max, z])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return
        
        #empty b3:5 Liter bottle to...
        if(z > 0):

            #empty b3:5 Liter bottle
            if([x, y, 0] not in visited):
                visited.append([x, y, 0])
                queue.append([x, y, 0])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

            #pour water from b3:5 Liter to b1:10 Liter,    keep remaining in b3:5 Liter
            if(((z + x) >= b1_max) and [b1_max, y, z - (b1_max - x)] not in visited):
                visited.append([b1_max, y, z - (b1_max - x)])
                queue.append([b1_max, y, z - (b1_max - x)])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

            #pour water from b3:5 Liter to b1:10 Liter,    no left over
            if(((z + x) <= b1_max) and [(x + z) , y, 0] not in visited):
                visited.append([(x + z) , y, 0])
                queue.append([(x + z) , y, 0])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

            #pour water from b3:5 Liter to b2:6 Liter,     keep remaining in b3:5 Liter
            if(((z + y) >= b2_max) and [x, b2_max, z - (b2_max - y)] not in visited):
                visited.append([x, b2_max, z - (b2_max - y)])
                queue.append([x, b2_max, z - (b2_max - y)])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return        

            #pour water from b3:5 Liter to b2:6 Liter,     no left over
            if(((z + y) <= b2_max) and [x, (y + z), 0] not in visited):
                visited.append([x, (y + z), 0])
                queue.append([x, (y + z), 0])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

        #fill b3:5 Liter bottle
        elif(z < b3_max):
            if([x, y, b3_max] not in visited):
                visited.append([x, y, b3_max])
                queue.append([x, y, b3_max])
                if(visited[-1] == goal_state):
                    output(explored, max_queue_length) 
                    return

#calculates path cost
def cost(current_path):
    path_cost = abs(current_path[0] - goal_state[0]) + abs(current_path[1] - goal_state[1]) + abs(current_path[2] - goal_state[2])
    return path_cost

#a* search
def astar():

    priority_queue = [[start_state, cost(start_state)]] #initialize priority queue and set a cost

    explored = 0 #counts number of nodes explored or popped
    max_queue_length = 1 #checks max length of queue

    #loop while priority queue list in not empty
    while priority_queue:
        
        priority_queue = sorted(priority_queue, key = lambda x: x[1]) #priority queue sorted by ascending order

        current = priority_queue.pop(0)[0] #remove last item from priority queue and save only current state in variable current

        explored += 1 #adds 1 to nodes explored or popped

        #calculated max length of priority queue
        if len(priority_queue) > max_queue_length:
                max_queue_length = len(priority_queue)

        #current water level of bottle b1, b2 and b3
        x = current[0] #b1
        y = current[1] #b2
        z = current[2] #b3

        #check if visited same as goal state
        if(visited[-1] == goal_state):
            output(explored, max_queue_length) 
            return

        #fill b1:10 Liter bottle
        if(x < b1_max and [b1_max, y, z] not in visited):
            visited.append([b1_max, y, z])
            priority_queue.append(([b1_max, y, z], cost([b1_max, y, z])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #fill b2:6 Liter bottle
        if(y < b2_max and [x, b2_max, z] not in visited):
            visited.append([x, b2_max, z])
            priority_queue.append(([x, b2_max, z], cost([x, b2_max, z])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return
        
        #fill b3:5 Liter bottle
        if(z < b3_max and [x, y, b3_max] not in visited):
            visited.append([x, y, b3_max])
            priority_queue.append(([x, y, b3_max], cost([x, y, b3_max])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #empty b1:10 Liter bottle
        if(x > 0 and [0, y, z] not in visited):
            visited.append([0, y, z])
            priority_queue.append(([0, y, z], cost([0, y, z])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #empty b2:6 Liter bottle       
        if(y > 0 and [x, 0, z] not in visited):
            visited.append([x, 0, z])
            priority_queue.append(([x, 0, z], cost([x, 0, z])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #empty b3:5 Liter bottle
        if(z > 0 and [x, y, 0] not in visited):
            visited.append([x, y, 0])
            priority_queue.append(([x, y, 0], cost([x, y, 0])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b1:10 Liter to b2:6 Liter,    keep remaining in b1:10 Liter       
        if(((x + y) >= b2_max and x > 0) and [x - (b2_max - y), b2_max, z] not in visited):
            visited.append([x - (b2_max - y), b2_max, z])
            priority_queue.append(([x - (b2_max - y), b2_max, z], cost([x - (b2_max - y), b2_max, z])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b1:10 Liter to b3:5 Liter,    keep remaining in b1:10 Liter
        if(((x + z) >= b3_max and x > 0) and [x - (b3_max - z), y, b3_max] not in visited):
            visited.append([x - (b3_max - z), y, b3_max])
            priority_queue.append(([x - (b3_max - z), y, b3_max], cost([x - (b3_max - z), y, b3_max])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b2:6 Liter to b1:10 Liter,    keep remaining in b2:6 Liter
        if(((y + x) >= b1_max and y > 0) and [b1_max, y - (b1_max - x), z] not in visited):
            visited.append([b1_max, y - (b1_max - x), z])
            priority_queue.append(([b1_max, y - (b1_max - x), z], cost([b1_max, y - (b1_max - x), z])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b2:6 Liter to b3:5 Liter,     keep remaining in b2:6 Liter
        if(((y + z) >= b3_max and y > 0) and [x, y - (b3_max - z), b3_max] not in visited):
            visited.append([x, y - (b3_max - z), b3_max])
            priority_queue.append(([x, y - (b3_max - z), b3_max], cost([x, y - (b3_max - z), b3_max])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b3:5 Liter to b1:10 Liter,    keep remaining in b3:5 Liter
        if(((z + x) >= b1_max and z > 0) and [b1_max, y, z - (b1_max - x)] not in visited):
            visited.append([b1_max, y, z - (b1_max - x)])
            priority_queue.append(([b1_max, y, z - (b1_max - x)], cost([b1_max, y, z - (b1_max - x)])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b3:5 Liter to b2:6 Liter,     keep remaining in b3:5 Liter
        if(((z + y) >= b2_max and z > 0) and [x, b2_max, z - (b2_max - y)] not in visited):
            visited.append([x, b2_max, z - (b2_max - y)])
            priority_queue.append(([x, b2_max, z - (b2_max - y)], cost([x, b2_max, z - (b2_max - y)])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b1:10 Liter to b2:6 Liter,    no left over
        if(((x + y) <= b2_max and x >= 0) and [0, (x + y), z] not in visited):
            visited.append([0, (x + y), z])
            priority_queue.append(([0, (x + y), z], cost([0, (x + y), z])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b1:10 Liter to b3:5 Liter,    no left over
        if(((x + z) <= b3_max and x >= 0) and [0, y, (x + z)] not in visited):
            visited.append([0, y, (x + z)])
            priority_queue.append(([0, y, (x + z)], cost([0, y, (x + z)])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b2:6 Liter to b1:10 Liter,    no left over
        if(((y + x) <= b1_max and y >= 0) and [(x + y), 0, z] not in visited):
            visited.append([(x + y), 0, z])
            priority_queue.append(([(x + y), 0, z], cost([(x + y), 0, z])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b2:6 Liter to b3:5 Liter,     no left over
        if(((y + z) <= b3_max and y >= 0) and [x, 0, (y + z)] not in visited):
            visited.append([x, 0, (y + z)])
            priority_queue.append(([x, 0, (y + z)], cost([x, 0, (y + z)])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b3:5 Liter to b1:10 Liter,    no left over
        if(((z + x) <= b1_max and z >= 0) and [(x + z) , y, 0] not in visited):
            visited.append([(x + z) , y, 0])
            priority_queue.append(([(x + z) , y, 0], cost([(x + z) , y, 0])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

        #pour water from b3:5 Liter to b2:6 Liter,     no left over
        if(((z + y) <= b2_max and z >= 0) and [x, (y + z), 0] not in visited):
            visited.append([x, (y + z), 0])
            priority_queue.append(([x, (y + z), 0], cost([x, (y + z), 0])))
            if(visited[-1] == goal_state):
                output(explored, max_queue_length) 
                return

#main functions
def main():
    while True:
        print("[1] Breadth First Search\n")
        print("[2] Depth First Search\n")
        print("[3] A* Search\n")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            bfs() #breadth first search
            break
        elif choice == 2:
            dfs() #depth first search
            break
        elif choice == 3:
            astar() #a* search
            break
        else:
            print("Please enter a valid input\n")    

main()                    