def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
