graph1 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

graph2 = {
    'a' : [],
    'b' : ['a'],
    'c' : ['a'],
    'd' : ['b', 'c', 'e'],
    'e' : ['h', 'r'],
    'f' : ['c', 'g'],
    'g' : [],
    'h' : ['p', 'q'],
    'p' : ['q'],
    's' : ['d','e', 'p'],
    'q' : [],
    'r' : ['f'],    
}

graph3 = {
    's': ['f', 'h'],
    'f': ['s', 'p'],
    'p': ['f', 'q'],
    'q': ['p', 'r'],
    'r': ['q', 't'],
    't': ['r', 'g'],
    'g': ['m', 't'],
    'm': ['d', 'n', 'g'],
    'n': ['m', 'e'],
    'e': ['d', 'n'],
    'd': ['e', 'm', 'b'],
    'b': ['a', 'd'],
    'a': ['b', 'c'],
    'c': ['a', 'k'],
    'k': ['c', 'h'],
    'h': ['s', 'k'],

}

graph4 = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E', 'G', 'F'],
    'E': ['D', 'G'],
    'F': ['D', 'G'],
    'G': ['D', 'E', 'F'],
}

def bfs(graph, start, end):
    """Trace the shortest path from start node to end node (if available)"""

    visited, paths = [], []
    # Start tracing path
    paths.append([start])

    while paths:
        # Trace to node via path and mark it as visited
        path = paths.pop(0) # pop first (FIFO) to emulate queue
        node = path[-1]
        visited.append(node)

        if node == end:
            return path

        # Extend current path toward neighbor node(s) and add to queue
        new_paths = [path+[n] for n in graph[node] if n not in visited]
        paths.extend(new_paths)

def dfs(graph, start, end):
    visited, paths = [], []
    # Start tracing path
    paths.append([start])

    while paths:
    # Trace to node via path and mark it as visited
        path = paths.pop() # pop last (FILO) to emulate stack
        node = path[-1]
        visited.append(node)

        if node == end:
            return path

        # Extend current path toward neighbor node(s) and add to stack
        new_paths = [path+[n] for n in graph[node] if n not in visited]
        paths.extend(new_paths)

    
# Driver Code
# print(bfs(graph1, 'A','F'))
# print(bfs(graph2, 's','g'))
# print(bfs(graph3, 's','g'))
# print(bfs(graph4, 'A','G'))
        
# print(dfs(graph1, 'A','F'))
# print(dfs(graph2, 's','g'))
# print(dfs(graph3, 's','g'))
# print(dfs(graph4, 'A','G'))