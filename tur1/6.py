from collections import deque


def add_edge(graph, u, v, length, safety):
    if u not in graph:
        graph[u] = []
    graph[u].append((v, length, safety))


def dfs(graph, start, best_cycle):
    visited = set()
    stack = deque([(start, start, [start], 0, 1)])

    while stack:
        current, origin, path, path_length, path_safety = stack.pop()

        for neighbour, length, safety in graph.get(current, []):
            if neighbour == origin and len(path) > 1:
                total_safety = path_safety * safety
                if total_safety >= 0.5 and total_safety <= 1:
                    cycle_length = path_length + length
                    if cycle_length > best_cycle['length'] or (
                            cycle_length == best_cycle['length'] and total_safety > best_cycle['safety']):
                        best_cycle['cycle'] = path + [origin]
                        best_cycle['length'] = cycle_length
                        best_cycle['safety'] = total_safety
            elif (current, neighbour) not in visited:
                total_safety = path_safety * safety
                if total_safety <= 1:
                    visited.add((current, neighbour))
                    stack.append((neighbour, origin, path + [neighbour], path_length + length, total_safety))


def find_best_cycle(graph, N):
    best_cycle = {'cycle': [], 'length': 0, 'safety': 1}  # Начинаем с максимально возможной безопасности
    for start in range(1, N + 1):
        dfs(graph, start, best_cycle)

    if best_cycle['cycle']:
        return best_cycle['cycle'], best_cycle['length'], round(best_cycle['safety'], 2)
    else:
        return "Нет подходящего маршрута"


N, M = map(int, input().split())
graph = {}
for _ in range(M):
    u, v, length, safety = map(float, input().split())
    add_edge(graph, int(u), int(v), length, safety)
    add_edge(graph, int(v), int(u), length, safety)

cycle, length, safety = find_best_cycle(graph, N)
if cycle:
    print(" ".join(map(str, cycle)), length, safety)
else:
    print("Нет подходящего маршрута")
