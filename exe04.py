# alunos = [
#     ["Bruno", [10, 8, 9]],
#     ["Rafael", [4, 7, 9]],
#     ["Carlos", [10, 10, 9]],
# ]

# print(alunos[1]) #Todas as informações do aluno no index 1

# print(alunos[1][0]) # Nome do aluno no index 1

# print(alunos[1][1]) # todas as notas

# print(alunos[1][1][1]) # segunda nota


# calcule a média de cada aluno.
# crie três listas:
    # aprovado: media >=7
    # recuperação: media >= 5 e media <7
    # reprovado: media < 5
# cada lista deve armazenar o nome do aluno e sua media

# exemplo esperado:

# aprovados = [["bruno",9.0]]
# reprovados = [["bento"], ["rute", 2.4]]

# Lista de alunos com nome e notas (corrigida com as vírgulas necessárias)
alunos = [
    ["Ana", [6.0, 5.5, 6.5]],
    ["Bruno", [10, 8, 9]],
    ["Bento", [3.0, 4.0, 2.5]],
    ["Rute", [2.0, 3.0, 2.2]],
    ["Rafael",[7.0, 10.0, 8.5]],
]

# Inicializa as três listas solicitadas
aprovados = []
recuperacao = []
reprovados = []

# Loop para percorrer cada aluno e calcular as médias
for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]
    
# Calcula a média do aluno atual
    media = sum(notas) / len(notas)
    media = round(media, 1) # Arredonda para 1 casa decimal igual ao exemplo
    
# Cria a sublista com o nome e a média calculada
    dados_aluno = [nome, media]
    
# Aplica as regras de classificação usando a estrutura if/elif/else
    if media >= 7.0:
        aprovados.append(dados_aluno)
    elif media >= 5.0 and media < 7.0:
        recuperacao.append(dados_aluno)
    else:
        reprovados.append(dados_aluno)

# Exibe os resultados na tela
print("Aprovados =", aprovados)
print("Recuperação =", recuperacao)
print("Reprovados =", reprovados)

