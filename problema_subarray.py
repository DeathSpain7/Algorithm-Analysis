# Importamos las bibliotecas necesarias
import time
import matplotlib.pyplot as plt
import numpy as np

def sub_suma_max(arr):
    max_suma = 0

    # Recorremos todos los posibles subarrays de la lista
    for i in range(len(arr)):
        sub_suma = 0
        for j in range(i, len(arr)):
            # Sumamos el número actual a la suma actual
            sub_suma += arr[j]

            # Si la suma actual es mayor que la suma máxima encontrada hasta ahora, la actualizamos
            if sub_suma > max_suma:
                max_suma = sub_suma

    return max_suma

# Creamos listas de diferentes tamaños
sizes = np.arange(1, 1001, 100)
execution_times = []

# Iniciamos el tiempo total de ejecución
total_start_time = time.perf_counter()

for size in sizes:
    # Creamos una lista de números aleatorios del tamaño actual
    numbers = np.random.randint(-10, 10, size)

    start_time = time.perf_counter()
    max_sum = sub_suma_max(numbers)
    execution_time = time.perf_counter() - start_time

    execution_times.append(execution_time)

# Calculamos el tiempo total de ejecución
total_execution_time = time.perf_counter() - total_start_time

# Creamos una gráfica para mostrar los tiempos de ejecución
plt.figure(figsize=(10, 6))
plt.plot(sizes, execution_times, color='blue')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Segundos')
plt.title('Tiempo de ejecución de la función sub_suma_max')
plt.show()

# Imprimimos el tiempo total de ejecución
print(f"El tiempo total de ejecución del programa fue de: {total_execution_time} segundos.")