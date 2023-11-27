def time_to_minutes(s):
    t = list(map(int, s.split(":")))
    return t[0] * 60 + t[1]


def time_diff(t1, t2):
    if t2 >= t1 + 90:
        return t2 - t1
    else:
        return t2 - t1 + 24 * 60


def time_add(t1, t2):
    return (t1 + t2) % (24 * 60)


def time_to_str(t):
    return str(t // 60) + ":" + str(t % 60).zfill(2)


def dfs(dep_city, ind_in_graph, graph, saved):  # time, length,
    city, dep_time, flight_time, flight_ind = graph[dep_city][ind_in_graph]
    arr_time = time_add(dep_time, flight_time)
    if city == "Malokribirsk":
        return True, flight_time, [city, dep_city]  # is reachable, time_to_reach "Malokribirsk"
    if saved[flight_ind] is None:
        is_reachable_local = False
        min_dest_time = 0  # значение не играет роли при сравнении, только для дефолтной ситуации
        optimal_path = []
        if city in graph:
            for next_ind_in_graph in range(len(graph[city])):
                next_city, next_dep_time, next_flight_time, next_flight_ind = graph[city][next_ind_in_graph]
                t_diff = time_diff(arr_time, next_dep_time)
                if t_diff >= 12 * 60:  # нет состыковки
                    continue
                is_reachable, time_to_dest, res_path = dfs(city, next_ind_in_graph, graph, saved)
                if is_reachable == True:  # нашли маршрут
                    if is_reachable_local == False:  # до этого маршрута не было -> сохраняем
                        is_reachable_local = True
                        min_dest_time = t_diff + time_to_dest
                        optimal_path = res_path.copy()
                    elif min_dest_time > t_diff + time_to_dest:  # is_reachable_local == True. Маршрут до этого был -> обновляем
                        min_dest_time = t_diff + time_to_dest
                        optimal_path = res_path.copy()
                elif is_reachable_local == False:  # is_reachable == False. До этого маршрута не было и машрут не нашли
                    if len(optimal_path) < len(res_path):  # проверяем, какой из сохраненных длиннее
                        min_dest_time = t_diff + time_to_dest
                        optimal_path = res_path.copy()
        min_dest_time += flight_time
        # ничего не нашли
        if optimal_path == []:
            optimal_path = [city, dep_city]
        else:
            optimal_path.append(dep_city)
        saved[flight_ind] = [is_reachable_local, min_dest_time, optimal_path]
    return saved[flight_ind]


N = int(input())
graph = {}
for i in range(N):
    row = input().split("|")
    graph.setdefault(row[0], [])
    graph[row[0]].append([row[1], time_to_minutes(row[2]), time_to_minutes(row[3]), i])

saved = [None] * N
default_city = "Moscow"
is_reachable_total = False
min_dest_time = 0  # значение не играет роли при сравнении, только для дефолтной ситуации
optimal_path = []
for ind_in_graph in range(len(graph[default_city])):
    is_reachable, time_to_dest, res_path = dfs(default_city, ind_in_graph, graph, saved)
    if is_reachable == True:
        if is_reachable_total == False:
            is_reachable_total = True
            min_dest_time = time_to_dest
            optimal_path = res_path.copy()
        elif min_dest_time > time_to_dest:
            min_dest_time = time_to_dest
            optimal_path = res_path.copy()
    elif is_reachable_total == False:
        if len(res_path) > len(optimal_path):
            min_dest_time = time_to_dest
            optimal_path = res_path.copy()
optimal_path.reverse()
print("|".join(optimal_path))
print(time_to_str(min_dest_time))
