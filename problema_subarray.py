# Importamos la biblioteca time para calcular el tiempo de ejecución
import time
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
# Declaramos la lista de numeros que vamos a utilizar
numbers = [1, -2, 3, 4, -5, 6, -7, 8, 9, -10]

start_time = time.perf_counter()
max_sum = sub_suma_max(numbers)

# Calculamos el tiempo de ejecución como la diferencia entre el tiempo actual y el tiempo de inicio
execution_time = time.perf_counter() - start_time

print(f"La suma máxima del subarray de la lista: {numbers} es: {sub_suma_max(numbers)}.")
print(f"El tiempo de ejecución fue de: {execution_time} segundos.")