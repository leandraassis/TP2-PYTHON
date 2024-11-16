def verificarNumero(numero):
    """Verifica se o parametro é um número maior ou igual a zero (positivo)

        retorno: boolean
    """
    return numero.isdigit()

def recebeNumeros():
    while(True):
        numero = input("Digite um número: ")
        if(verificarNumero(numero)):
            print("Número VÁLIDO. Obrigada.")
            break
        else:
            print("Caractere ou número INVÁLIDO, tente novamente.")

recebeNumeros()