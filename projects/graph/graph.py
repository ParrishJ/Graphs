"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    # Adding remove_vertex method for future reference
    def remove_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            print("Vertex Not Found")
            return
        self.vertices.pop(vertex_id)
        for vertex in self.vertices:
            self.vertices[vertex].discard(vertex_id)

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            print("Edge cannot be added to nodes that do not exist")
            return
        self.vertices[v1].add(v2)

    # Adding remove_edge for future reference
    def remove_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            print("Edge cannot be removed to nodes that do not exist")
            return
        self.vertices[v1].discard(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currentNode = queue.popleft()
            if currentNode not in visited:
                visited.add(currentNode)
                print(currentNode)
                for neighbor in self.vertices[currentNode]:
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            currentNode = stack.pop()
            if currentNode not in visited:
                visited.add(currentNode)
                print(currentNode)
                for neighbor in self.vertices[currentNode]:
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        
        def helper(starting_vertex):
            visited.add(starting_vertex)
            
            neighbors = list(self.get_neighbors(starting_vertex))
            neighbors.reverse()
            for neighbor in neighbors:
                if neighbor not in visited:
                    print(neighbor)
                    helper(neighbor)
        print(starting_vertex)
        helper(starting_vertex)
        return
        
    
   

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = deque()
        queue.append([starting_vertex])
        while len(queue) > 0:
            currentPath = queue.popleft()
            currentNode = currentPath[-1]
            if currentNode == destination_vertex:
                return currentPath
            if currentNode not in visited:
                visited.add(currentNode)
                print(currentNode)
                for neighbor in self.vertices[currentNode]:
                    newPath = list(currentPath)
                    newPath.append(neighbor)
                    queue.append(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        visited = set()
        stack = deque()
        stack.append([starting_vertex])
        while len(stack) > 0:
            currentPath = stack.pop()
            currentNode = currentPath[-1]
            if currentNode == destination_vertex:
                return currentPath
            if currentNode not in visited:
                visited.add(currentNode)
                print(currentNode)
                for neighbor in self.vertices[currentNode]:
                    newPath = list(currentPath)
                    newPath.append(neighbor)
                    stack.append(newPath) 
            
        
        

    def dfs_recursive(self, starting_vertex, destination_vertex):
        
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        def helper(currentPath, destination_vertex):
            currentNode = currentPath[-1]

            if currentNode == destination_vertex: 
                return currentPath
            if currentNode not in visited:
                visited.add(currentNode)
                print(currentNode)
                for neighbor in self.vertices[currentNode]:
                    newPath = list(currentPath)
                    newPath.append(neighbor)
                return helper(newPath, destination_vertex)
        return helper([starting_vertex], destination_vertex) 

    def __repr__(self):
        print(f"{self.vertices}")

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
