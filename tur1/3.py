from collections import deque


def find_longest_route(to_flight, start):
    visit = set()
    mx_route = []
    mx_time = 0

    queue = deque([(start, [start], 0)])

    while queue:
        sity, route, time = queue.popleft()
        visit.add(sity)

        if len(route) > len(mx_route) or (len(route) == len(mx_route) and time > mx_time):
            mx_route = route
            mx_time = time

        for flight in to_flight.get(sity, []):
            nasnach, time = flight
            if nasnach not in visit:
                new_route = route + [nasnach]
                new_time = time + time
                queue.append((nasnach, new_route, new_time))

    return mx_route, mx_time


N = int(input())
flights = {}

for _ in range(N):
    departure, arrival, time = input().split('|')
    time = int(time)
    if departure not in flights:
        flights[departure] = []
    flights[departure].append((arrival, time))

max_route = []
max_time = 0

for city in flights.keys():
    current_route, current_time = find_longest_route(flights, city)
    if len(current_route) > len(max_route) or (len(current_route) == len(max_route) and current_time > max_time):
        max_route = current_route
        max_time = current_time

# Вывод маршрута и времени
print('|'.join(max_route))
print(max_time)
