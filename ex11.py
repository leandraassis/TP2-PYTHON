listaNumeros = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]

def receberNumero():
    """Recebe um número digitado pelo usuário

        retorno: int
    """
    try:
        numero = int(input("Digite um número: "))
        return numero
    except:
        print("Erro: digite um número e tente novamente.")

def buscarElemento(lista, numero):
    """Busca a presença de um item numa lista

    parametros: lista (list), numero (int)

    retorno: (int) retorna -1 se item não for encontrado e seu indice se for
    """ 
    if(numero in lista):
        return lista.index(numero)
    else:
        return -1

print(buscarElemento(listaNumeros, receberNumero()))