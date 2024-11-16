listaUm = [1, 2, 3, 4, 5, 6, 7, 8]
listaDois = [10, 20, 30, 40, 50, 60, 70, 80]

def somarListas(lista1, lista2):
    """Soma os items de duas listas

        parametros: lista1 (list), lista2 (list)

        retorno: list
    """
    somaListas = []
    for i in range(len(lista1)):
        somaListas.append(lista1[i] + lista2[i])
    return somaListas

print(somarListas(listaUm, listaDois))
# [11, 22, 33, 44, 55, 66, 77, 88]
