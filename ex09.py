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

def listaInvertida(lista):
    """Inverte e exibe a lista invertida

        parametros: lista (list)
    """
    listaInvertida = lista[::-1]
    print(listaInvertida)

listaInvertida(receberNumeros())