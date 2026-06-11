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
    ["Ricardo", [5.0, 6.5, 4.8],]
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

# # Aqui está a explicação detalhada de cada linha do código, para você entender perfeitamente como ele funciona para a sua prova:python# Lista de alunos com nome e notas (corrigida com as vírgulas necessárias)
# alunos = [
#     ["Ana", [6.0, 5.5, 6.5]],
#     ["Bruno", [10, 8, 9]],
#     ["Bento", [3.0, 4.0, 2.5]],
#     ["Rute", [2.0, 3.0, 2.2]]
# ]
# Use o código com cuidado.Linhas 2 a 7: Criam uma matriz (uma lista de listas) chamada alunos. Cada elemento interno contém o nome do aluno no índice 0 e uma lista com suas três notas no índice 1. As vírgulas ao final de cada linha evitam aquele erro de sintaxe.python# Inicializa as três listas solicitadas
# aprovados = []
# recuperacao = []
# reprovados = []
# Use o código com cuidado.Linhas 10 a 12: Criam três listas vazias usando []. Elas servirão como "pastas" para guardar os alunos filtrados mais adiante.python# Loop para percorrer cada aluno e calcular as médias
# for aluno in alunos:
# Use o código com cuidado.Linha 15: O comando for aluno in alunos: inicia um laço de repetição. Ele vai ler a lista alunos item por item. A cada repetição, a variável temporária aluno vai carregar os dados de um estudante (primeiro a Ana, depois o Bruno, etc.).python    nome = aluno[0]
#     notas = aluno[1]
# Use o código com cuidado.Linhas 16 e 17:aluno[0] pega o primeiro elemento da sublista atual (o texto com o nome do aluno) e guarda na variável nome.aluno[1] pega o segundo elemento (a lista com as notas) e guarda na variável notas.python    # Calcula a média do aluno atual
#     media = sum(notas) / len(notas)
#     media = round(media, 1) # Arredonda para 1 casa decimal igual ao exemplo
# Use o código com cuidado.Linhas 20 e 21:sum(notas) soma as notas do aluno./ len(notas) divide essa soma pela quantidade de notas (que é 3), descobrindo a média.round(media, 1) arredonda o resultado para exibir apenas uma casa decimal (ex: 6.3 em vez de 6.33333333).python    # Cria a sublista com o nome e a média calculada
#     dados_aluno = [nome, media]
# Use o código com cuidado.Linha 24: Monta uma nova listinha contendo apenas o nome do estudante e a média que acabamos de calcular (ex: ["Ana", 6.0]).python    # Aplica as regras de classificação usando a estrutura if/elif/else
#     if media >= 7.0:
#         aprovados.append(dados_aluno)
# Use o código com cuidado.Linhas 27 e 28: O if testa se a média é maior ou igual a 7.0. Se for verdade, ele usa o append() para injetar a listinha dados_aluno dentro da lista global aprovados.python    elif media >= 5.0 and media < 7.0:
#         recuperacao.append(dados_aluno)
# Use o código com cuidado.Linhas 29 e 30: Caso a média seja menor que 7, o elif entra em ação e checa a segunda condição: se a média está entre 5.0 (inclusive) e 7.0 (exclusive). Se positivo, faz o append na lista de recuperacao.python    else:
#         reprovados.append(dados_aluno)
# Use o código com cuidado.Linhas 31 e 32: O else captura qualquer aluno que não entrou nas regras anteriores (ou seja, quem ficou com média abaixo de 5.0) e faz o append na lista de reprovados.python# Exibe os resultados na tela
# print("Aprovados =", aprovados)
# print("Recuperação =", recuperacao)
# print("Reprovados =", reprovados)
# Use o código com cuidado.Linhas 35 a 37: Essas linhas estão fora do loop for (repare que não têm espaços/indentação no começo). Elas rodam apenas uma vez no final do programa para mostrar os resultados organizados no terminal.