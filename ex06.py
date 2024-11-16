def numeroPrimo(numero):
    """Verfica se um número é primo
    
        parametros: numero (int)

        retorno: boolean
    """
    if (numero <= 1):
        return False
    for i in range(2, numero):
        if (numero % i == 0):
            return False
    return True

def processaNumeros():
    try:
        numeroUm = int(input("Digite o primeiro número: "))
        numeroDois = int(input("Digite o segundo número: "))
        
        qtdPrimos = 0
        listaPrimos = []
        for i in range(numeroUm, numeroDois + 1):
            primo = numeroPrimo(i)
            if(primo):
                qtdPrimos += 1
                listaPrimos.append(i)
        print(f"Quantidade: {qtdPrimos} números primos\n")
        print("Números primos encontrados: ")
        for primo in listaPrimos:
            print(f"{primo}")
    except:
        print("Erro: por favor, digite apenas números e tente novamente.")


processaNumeros()