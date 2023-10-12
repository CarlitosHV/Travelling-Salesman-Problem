import random
import time
import matplotlib.pyplot as plt

city_names = ["Guanajuato", "León", "Celaya", "Irapuato", "Silao", "San Miguel de Allende", "Dolores Hidalgo",
              "Salamanca", "Valle de Santiago", "Cuerámaro", "Abasolo"]

connections = [
    [(1, 29), (2, 20), (3, 21), (4, 16), (5, 31), (6, 100), (7, 12), (8, 4), (9, 31), (10, 120)],
    [(0, 29), (2, 15), (3, 29), (4, 28), (5, 40), (6, 72), (7, 21), (8, 29), (9, 41), (10, 60)],
    [(0, 20), (1, 15), (3, 15), (4, 14), (5, 25), (6, 81), (7, 9), (8, 23), (9, 27), (10, 20)],
    [(0, 21), (1, 29), (2, 15), (4, 4), (5, 12), (6, 92), (7, 12), (8, 25), (9, 13), (10, 15)],
    [(0, 16), (1, 28), (2, 14), (3, 4), (5, 16), (6, 94), (7, 9), (8, 20), (9, 16), (10, 2)],
    [(0, 31), (1, 40), (2, 25), (3, 12), (4, 16), (6, 95), (7, 24), (8, 36), (9, 3), (10, 70)],
    [(0, 100), (1, 72), (2, 81), (3, 92), (4, 94), (5, 95), (7, 90), (8, 101), (9, 99), (10, 80)],
    [(0, 12), (1, 21), (2, 9), (3, 12), (4, 9), (5, 24), (6, 90), (8, 15), (9, 25), (10, 40)],
    [(0, 4), (1, 29), (2, 23), (3, 25), (4, 20), (5, 36), (6, 101), (7, 15), (9, 35), (10, 96)],
    [(0, 31), (1, 41), (2, 27), (3, 13), (4, 16), (5, 3), (6, 99), (7, 25), (8, 35), (10, 50)],
    [(0, 31), (1, 41), (2, 27), (3, 13), (4, 16), (5, 3), (6, 99), (7, 25), (8, 35), (9, 25)]
]


def calculate_total_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += [conn[1] for conn in connections[path[i]] if conn[0] == path[i + 1]][0]
    total_distance += [conn[1] for conn in connections[path[-1]] if conn[0] == path[0]][
        0]
    return total_distance


def random_shortest_path(iterations, start_city):
    shortest_distance = float('inf')
    shortest_path = []

    for _ in range(iterations):
        path = [start_city] + random.sample([i for i in range(len(connections)) if i != start_city],
                                            len(connections) - 1)
        distance = calculate_total_distance(path)

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    return shortest_path, shortest_distance


iterations = 100000
print("Elige una ciudad como punto de partida:")
for i, city in enumerate(city_names):
    print(f"{i + 1}. {city}")

start_city_index = int(input()) - 1

start_time = time.time()
shortest_path, shortest_distance = random_shortest_path(iterations, start_city_index)
end_time = time.time()

print("Camino más corto:")
for city_index in shortest_path:
    print(city_names[city_index])
print("Distancia total:", shortest_distance)

execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")

travel_times = []

# Iterar sobre todas las ciudades de destino
for dest_city_index in range(len(city_names)):
    if dest_city_index == start_city_index:
        continue  # Saltar la ciudad de partida

    start_time = time.time()
    shortest_path, shortest_distance = random_shortest_path(iterations, start_city_index)
    end_time = time.time()

    travel_time = end_time - start_time
    travel_times.append(travel_time)

    print(f"De {city_names[start_city_index]} a {city_names[dest_city_index]} tardó {travel_time} segundos")

# Crear la gráfica de barras
plt.bar(city_names[:start_city_index] + city_names[start_city_index + 1:], travel_times)
plt.title(f"Tiempo de viaje desde {city_names[start_city_index]} a otras ciudades")
plt.xlabel("Ciudad de destino")
plt.ylabel("Tiempo de viaje (segundos)")
plt.xticks(rotation=45)
plt.show()













