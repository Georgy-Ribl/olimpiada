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
            mx_route, mx_time = route, time

        for nasnach, flight_time in to_flight.get(sity, []):
            if nasnach not in visit:
                new_route, new_time = route + [nasnach], time + flight_time
                queue.append((nasnach, new_route, new_time))

    return mx_route, mx_time


N = int(input())
flights = {}

for _ in range(N):
    departure, arrival, time = input().split('|')
    time = int(time)
    flights.setdefault(departure, []).append((arrival, time))

max_route, max_time = [], 0

for city in flights:
    current_route, current_time = find_longest_route(flights, city)
    if len(current_route) > len(max_route) or (len(current_route) == len(max_route) and current_time > max_time):
        max_route, max_time = current_route, current_time

print('|'.join(max_route))
print(max_time)
