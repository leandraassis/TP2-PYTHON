listaNumeros = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

def processaLista(lista):
    """Encontra o maior, menor, soma e média dos numeros de uma lista

        parametros: lista (list)
    """
    soma = 0
    for numero in listaNumeros:
        soma += numero
    media = soma /len(lista)

    maior = max(listaNumeros)
    menor = min(listaNumeros)
    print(f"Menor: {menor}")
    print(f"Maior: {maior}")
    print(f"Soma: {soma}")
    print(f"Média: {media}")

processaLista(listaNumeros)

