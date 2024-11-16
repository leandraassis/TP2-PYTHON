def calcularFatorial(numero):
    """Calcula o fatorial de um número
    
    parametros: numero (int)

    retorno: int
    """
    if (numero == 0 or numero == 1):
        return 1
    else:
        return numero * calcularFatorial(numero - 1)
    

def receberNumeros():
    """Recebe e armazena em lista os numeros digitados pelo usuario
    
    retorno: list
    """
    fatoriaisLista = []
    while(True):
        numeroDigitado = input("Digite um número inteiro positivo (0 para sair): ")
        if (numeroDigitado.isdigit() == False):
            print("Erro: valor ou caractere não aceito.")
            continue
        numeroDigitado = int(numeroDigitado)
        if(numeroDigitado == 0):
            fatoriaisLista.append(numeroDigitado)
            break
        else: 
            fatoriaisLista.append(numeroDigitado)
    return fatoriaisLista

def exibirFatorial(numeroLista):
    """Exibe os fatoriais dos numeros recebidos
    
    parametros: numeroLista (list)
    """
    for item in numeroLista:
        print(f"Fatorial de {item}: {calcularFatorial(item)}")
    

exibirFatorial(receberNumeros())