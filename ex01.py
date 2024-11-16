def verificadorVogais():
    """Verifica se um (1) caractere digitado é uma vogal"""
    vogais = ["a", "e", "i", "o", "u"]
    vogaisContagem = 0
    while(True):
        caractereDigitado = input("Entre com um caractere: ")
        caractereDigitado = caractereDigitado.lower()
        if (len(caractereDigitado) != 1):
            print("Por favor, entre com apenas UM caractere.")
            continue
        elif (caractereDigitado == "."):
            print(f"Número de vogais: {vogaisContagem}")
            break
        else:
            if (caractereDigitado in vogais):
                vogaisContagem += 1

verificadorVogais()