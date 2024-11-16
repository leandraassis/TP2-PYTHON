listaNumeros = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

def paresImpares():
    """Filtra os números pares e impares de uma lista e os exibe"""
    pares = []
    impares = []
    for numero in listaNumeros:
        if(numero % 2 == 0):
            pares.append(numero)
        else:
            impares.append(numero)
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")

paresImpares()