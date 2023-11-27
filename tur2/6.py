N, M, K = map(int, input().split())
graph = {}
for i in range(M):
    node1, node2, length, sec = input().split()
    node1 = int(node1)
    node2 = int(node2)
    length = int(length)
    sec = float(sec)
    if node1 != node2:
        graph.setdefault(node1, [])
        graph.setdefault(node2, [])
        graph[node1].append([node2, length, sec])
        graph[node2].append([node1, length, sec])
for_visit = set()
for k in range(K):
    for_visit.add(int(input()))


def bctr(node, path, visited, length, security, for_visit, graph, results):
    if 2 * len(visited) >= len(for_visit):
        if len(path) > len(results[0]):
            results[0] = path.copy()
            results[1] = security
            results[2] = length
        elif len(path) == len(results[0]) and security > results[1]:
            results[0] = path.copy()
            results[1] = security
            results[2] = length
    if node in graph:
        for next_node_row in graph[node]:
            next_node, pair_length, sec = next_node_row
            if sec * security >= 0.5 and next_node not in path:
                path.append(next_node)
                if next_node in for_visit:
                    visited.add(next_node)
                bctr(next_node, path, visited, length + pair_length, sec * security, for_visit, graph, results)
                path.pop()
                visited.discard(next_node)


results = [[], 0, 0]
for node in graph:
    visited = set()
    if node in for_visit:
        visited.add(node)
    bctr(node, [node], visited, 0, 1, for_visit, graph, results)
if results[0][0] > results[0][-1]:
    results[0].reverse()
print(*results[0], end=" ")
print(results[2], end=" ")
print("%.2f" % results[1])
