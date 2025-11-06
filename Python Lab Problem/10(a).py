def find(parent, i): 
    if parent[i] != i: 
        parent[i] = find(parent, parent[i]) 
    return parent[i] 
def union(parent, rank, x, y): 
    xroot, yroot = find(parent, x), find(parent, y) 
    if rank[xroot] < rank[yroot]: 
        parent[xroot] = yroot 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] = xroot 
    else: 
        parent[yroot] = xroot 
        rank[xroot] += 1 
def kruskal(graph): 
    result, parent, rank = [], [], [] 
    for node in range(len(graph)): 
        parent.append(node) 
        rank.append(0) 
    edges = sorted(graph, key=lambda item: item[2]) 
    e = 0 
    i = 0 
    while e < len(graph)-1 and i < len(edges): 
        u, v, w = edges[i] 
        i += 1 
        x, y = find(parent, u), find(parent, v) 
        if x != y: 
            e += 1 
            result.append((u, v, w)) 
            union(parent, rank, x, y) 
    return result 
graph = [(0, 1, 10), (1, 2, 5), (0, 2, 6)] 
print(kruskal(graph))