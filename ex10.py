def receberNumeros():
    """Recebe números e coloca numa lista
    
        retorno: list - com os numeros recebidos
    """
    listaNumeros = []
    try:
        while(True):
            numero = int(input("Digite um número(0 para encerrar): "))
            listaNumeros.append(numero)
            if(numero == 0):
                break
        return listaNumeros
    except:
        print("Erro: por favor, digite apenas números.")


def mediaLista(lista):
    """Calcula a media da soma dos items de uma lista
    
        parametros: lista (list)

        retorno: media (int)
    """
    qtdItems = len(lista)
    soma = 0
    for item in lista:
        soma += item
    media = soma/qtdItems
    return media


def mostrarListaFiltrada(listaBruta):
    """Mostra a lista filtrada com apenas os numeros acima de uma media

        parametros: listaBruta (list)
    """
    media = mediaLista(listaBruta)

    listaFiltrada = filter(lambda numero: numero > media, listaBruta)

    print(list(listaFiltrada))
    

mostrarListaFiltrada(receberNumeros())