def definirProgressao():
    """Recebe os números e define a progressão
    
        retorno: (list) onde [0]n1, [1]n2, [2]progressao
    """
    numeros = []
    try:
        numeroUm = int(input("Digite o primeiro número: "))
        numeroDois = int(input("Digite o segundo número: "))

        progressao = numeroDois - numeroUm
        numeros.append(numeroUm) #[0]
        numeros.append(numeroDois)#[1]
        numeros.append(progressao)#[2]

        return numeros
    except:
        print("Erro: apenas números são aceitos. Tente novamente:")

def mostrarProgressao(listaNumeros):
    """Mostr os primeiros 10 termos da progressão aritmética
    
        parametros: listaNumeros(list)
    """
    numeroUm = listaNumeros[0]
    numeroDois = listaNumeros[1]
    progressao = listaNumeros[2]

    print(numeroUm)
    print(numeroDois)
    for i in range(1, 11):
        numeroDois += progressao
        print(numeroDois)


mostrarProgressao(definirProgressao())