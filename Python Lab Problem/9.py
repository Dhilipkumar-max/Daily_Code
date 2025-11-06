import heapq 
def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
    visited = set() 
    heap = [(0, start)] 
    while heap: 
        curr_dist, curr_node = heapq.heappop(heap) 
        if curr_node in visited: 
            continue 
        visited.add(curr_node) 
        for neighbor, weight in graph[curr_node].items(): 
            distance = curr_dist + weight 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
 
                heapq.heappush(heap, (distance, neighbor)) 
    return distances 
# Example graph 
graph = { 
    'A': {'B': 5, 'C': 2}, 
    'B': {'D': 1}, 
    'C': {'B': 8, 'D': 7}, 
    'D': {} 
} 
print(dijkstra(graph, 'A')) 