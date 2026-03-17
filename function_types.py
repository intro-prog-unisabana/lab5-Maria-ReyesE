def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    
    return float(promedio)

#Ejercicio 3
def list_shift(lista, valor):
    for i in range(len(lista)):
        lista[i] += valor


def calc_avg(lista):
    return sum(lista) / len(lista)


def print_normalized(lista):
    print(lista)
    