N, M, K = map(int, input().split())
graph = {}
for i in range(M):
    node1, node2, length, sec = input().split()
    node1 = int(node1)
    node2 = int(node2)
    length = int(length)
    sec = float(sec)
    if node1 != node2:
        graph.setdefault(node1, set())
        graph.setdefault(node2, set())
        graph[node1].add((node2, length, sec))
        graph[node2].add((node1, length, sec))
for k in range(K):
    not_for_visit = int(input())
    if not_for_visit in graph:
        for el in graph[not_for_visit]:
            for next_node in graph[el[0]]:
                if next_node[0] == not_for_visit:
                    graph[el[0]].remove(next_node)
                    if not graph[el[0]]:
                        del graph[el[0]]
                    break
        del graph[not_for_visit]


def bctr(path, length, security, graph, results):
    if len(path) > len(results[0]):
        results[0] = path.copy()
        results[1] = security
        results[2] = length
    elif len(path) == len(results[0]) and security > results[1]:
        results[0] = path.copy()
        results[1] = security
        results[2] = length
    node = path[-1]
    if node in graph:
        for next_node_row in graph[node]:
            next_node, pair_length, sec = next_node_row
            if sec * security >= 0.5 and next_node not in path:
                path.append(next_node)
                bctr(path, length + pair_length, sec * security, graph, results)
                path.pop()


results = [[], 0, 0]
for node in graph:
    visited = set()
    bctr([node], 0, 1, graph, results)
if results[0][0] > results[0][-1]:
    results[0].reverse()
print(*results[0], end=" ")
print(results[2], end=" ")
print("%.2f" % results[1])
