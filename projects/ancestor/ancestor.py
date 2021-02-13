"""
UNDERSTAND
**********

We are given a list of tuples where the first item in the tuple represents the "parent" of a "descendant" 
which is represented by the second number in the tuple. Our task is to create an algorithm that will 
use this list to determine the oldest "ancestor" of the item that we are given to start with.

PLAN
****

To accomplish this goal, we will construct a graph from the data then do a depth first traversal to find the 
"oldest" ancestor / terminal end of the graph.

In this case, the vertices of the graph will be the "descendants" (the second number in each tuple) and the edges 
will be the "parents" (the first number in each tuple). Once we have the graph in place, we can do a depth first traversal 
with some special checks in place to find the oldest ancestor. 

"""

from collections import deque
def earliest_ancestor(ancestors, starting_node):

    # Generates our graph
    def createAncestorGraph(ancestors):
        graph = {}
        for edge in ancestors:
            ancestor, descendant = edge[0], edge[1]
            if descendant in graph:
                graph[descendant].add(ancestor)
                    
            else:
                graph[descendant] = { ancestor }
        return graph
        
    graph = createAncestorGraph(ancestors)
    stack = deque()
    visited = set()
    stack.append(starting_node)
    
    #Returns -1 if the starting node has no parent
    if starting_node not in graph:
        return -1

    # Depth First Traversal Here
    else: 
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                last = current
                visited.add(current)
                
                if current not in graph:
                    pass
                else:
                    # Before we push our neighbors to the stack, we want to order them so that we push the neighbor with the smallest value first,
                    # which will ensure that we return the smaller of the two in the event that they are both the "oldest ancestor".
                    stack_list = [] 
                    for neighbor in graph[current]:
                        stack_list.append(neighbor)
                    sorted_list = sorted(stack_list)
                    for item in sorted_list:
                        stack.append(item)
        return last


