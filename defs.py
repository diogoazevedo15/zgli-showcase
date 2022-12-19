#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def bfs_dfs_search(args):
    
    graf = args[0]
    start = args[1]
    end = args[2]
    option = args[3]
    
    # print(f'Searching from {start} to {end}')
    
    # Initialize queue. Queue starts by only having the 'start node'.
    queue = [(start,[start])]
    cicle = 1
    
    while queue:
        head = queue[0]  #(start,[start])
        rest = queue[1:] #[(ex1,[ex1]),(ex2,[ex2]),(ex3,[ex3]), ...]
        
        # If end reached, stop search
        if head[0] == end:
            break
            
        else:
            # Get ajacent noeds. They come in a tupule.
            expand = graf[head[0]] #('A',['A']) #( 'C' , 'B' )
            
            # Turn the tupule into an array so we can eddit it.
            expand = list(expand)
            
            # Expand format is as follows: (Adjacent,[pathToThisAdjacentNode])
            addToQueue = []
            for i, point in enumerate(expand):
                if point not in head[1]:
                    # Here we use o 'path + node' and not the .append().
                    # Check out the difference here: https://stackoverflow.com/questions/10748158/why-does-not-the-operator-change-a-list-while-append-does
                    addToQueue.append((expand[i],head[1] + [point]))
            
            # DFS: Depth first search   
            if option == 0: 
                queue = sorted(addToQueue) + rest
            
            # Breath first seach
            else: 
                queue = rest + sorted(addToQueue)
        
        # Cicle count if the user wants to see how many iterations it took
        cicle = cicle + 1
        
    return head[1][1:-1]

