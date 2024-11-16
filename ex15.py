def receberAlunos():
    """Recebe nome e notas de alunos e armazena em uma lista

        retorno: list - lista de alunos
    """
    listaAlunos = []

    while(True):
        aluno = []
        nome = input("Digite o nome do aluno: ")
        if(nome.lower() == "fim"):
            break

        while(True):
            try:
                nota1 = float(input(f"Digite a primeira nota do aluno {nome}: "))
                if(nota1 < 0 or nota1 > 10):
                    print("Nota inválida. A nota deve estar entre 0 e 10.")
                    continue
                break
            except:
                print("Por favor, insira um número válido para a nota.")
                
        while(True):
            try:
                nota2 = float(input(f"Digite a segunda nota do aluno {nome}: "))
                if(nota2 < 0 or nota2 > 10):
                    print("Nota inválida. A nota deve estar entre 0 e 10.")
                    continue
                break
            except:
                print("Por favor, insira um número válido para a nota.")
        aluno.append(nome)
        aluno.append(nota1)
        aluno.append(nota2)
        listaAlunos.append(aluno)

    return listaAlunos

def definirMedias(lista):
    """Calcula a média de alunos

        parametros: lista (list) - lista de alunos com seus nomes e notas

        retorno: list - medias de alunos
    """
    listaMedias = []
    for aluno in lista:
        alunoIdentificado = []
        nome = aluno[0]
        nota1 = aluno[1]
        nota2 = aluno[2]
        mediaAluno = (nota1 + nota2) / 2
        alunoIdentificado.append(nome)
        alunoIdentificado.append(mediaAluno)
        listaMedias.append(alunoIdentificado)
    return listaMedias

def mediaTurma(lista):
    """Calcula a média de uma turma baseado na média de alunos

        parametos: list - lista de médias de alunos

        retorno: list - media da turma
    """
    soma = 0
    for media in lista:
        soma += media[1]
    mediaTurma = soma / len(lista)
    return mediaTurma
    

def mostrarResultados():
    """Exibe as médias dos alunos e a média da turma"""
    listaAlunos = receberAlunos()
    medias = definirMedias(listaAlunos)
    mediaDaTurma = mediaTurma(medias)
    for aluno in medias:
        nome = aluno[0]
        mediaAluno = aluno[1]
        print(f"Aluno: {nome} - Média: {round(mediaAluno, 1)}")
    print(f"Média da turma: {mediaDaTurma}")

mostrarResultados()
