def somaUmCem():
    """Calcula a soma dos números de 1 a 100
    
        retorno:
        int - soma
    """
    soma = 0
    for i in range(1, 101):
        soma += i
    return soma


def mediaUmCem(soma):
    """Calcula a média da soma dos números de 1 a 100
    
        retorno:
        float - media
    """
    media = soma / 100
    return media

def mostrarResultados(soma, media):
    """Exibe dois números
    
        parametros:
        soma (int)
        media (float)
    """
    print(f"Soma: {soma}")
    print(f"Média: {media}")

mostrarResultados(somaUmCem(), mediaUmCem(somaUmCem()))