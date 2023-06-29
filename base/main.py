import random


def sum(a, b):
    return a + b


def mult(a, b):
    return a * b


def generate_random_array(n):
    random_array = []
    for i in range(0, n):
        random_number = random.randint(0, i)
        random_array.append(random_number)
    return random_array


if __name__ == '__main__':
    # test de las funciones. Si quiere hacer mas pruebas modifique el rango en el siguiente for loop:
    for i in range(0, 5):
        print(f"Inicio de la prueba {i+1}:")
        # funcion que suma dos numeros
        print(f"Funcion suma: {sum(random.randint(i, 100), random.randint(i, 100))}")
    # function multiplicar dos numeros ingresados
        print(f"Funcion multiplicar: {mult(random.randint(i, 100), random.randint(i, 100))}")
    # funcion que genera una lista de numeros aleatorios de longitud variable
        print(f"Funcion generacion lista numeros aleatorios: {generate_random_array(random.randint(i, 10))}")
        print(f"fin de la prueba {i+1} \n")
