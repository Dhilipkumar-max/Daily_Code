from heapq import heappush, heappop 
def prim(graph): 
    min_spanning_tree = [] 
    visited = set() 
    start_vertex = list(graph.keys())[0] 
    priority_queue = [(weight, start_vertex, neighbor) for neighbor, weight in 
graph[start_vertex]] 
    heappush(priority_queue, (0, None, start_vertex)) 
    while priority_queue: 
        weight, parent, current_vertex = heappop(priority_queue) 
        if current_vertex not in visited: 
            visited.add(current_vertex) 
            if parent is not None: 
                min_spanning_tree.append((parent, current_vertex, weight)) 
            for neighbor, edge_weight in graph[current_vertex]: 
                if neighbor not in visited: 
                    heappush(priority_queue, (edge_weight, current_vertex, neighbor)) 
    return min_spanning_tree 
graph = { 
    'A': [('B', 2), ('C', 1)], 
    'B': [('A', 2), ('D', 3), ('E', 1)], 
    'C': [('A', 1), ('D', 4)], 
    'D': [('B', 3), ('C', 4), ('E', 1)], 
    'E': [('B', 1), ('D', 1)] 
} 
minimum_spanning_tree = prim(graph) 
print("Minimum Spanning Tree:") 
print(minimum_spanning_tree)
