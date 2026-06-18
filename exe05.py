tupla = (1, 2, 3, 4, 5)
# Acessando elementos da tupla
print(tupla[0])  # Imprime o primeiro elemento (1)
print(tupla[2])  # Imprime o terceiro elemento (3)
print(tupla[-1]) # Imprime o último elemento (5)    



print(tupla)

alunos = ("bruno", "rafael", "carlos")
print(alunos[0])  # Imprime o primeiro aluno (bruno)
print(alunos[1])  # Imprime o segundo aluno (rafael)
print(alunos[2])  # Imprime o terceiro aluno (carlos)

# alunos [0] = "ana"  # Isso causará um erro, pois tuplas são imutáveis


cor = ("vermelho", "verde", "azul", "amarelo", "roxo")
print(cor[0])  # Imprime o primeiro elemento (vermelho)
print(cor[2])  # Imprime o terceiro elemento (azul) 
print(cor[-1]) # Imprime o último elemento (roxo)

print(cor [1:3]) # Imprime o segundo e terceiro elementos (verde e azul)


# print(cor[6])  # Isso causará um erro, pois o índice 6 está fora do alcance da tupla

# cor [2] = "laranja"  # Isso causará um erro, pois tuplas são imutáveis

for index in range(0,5):
    print(cor[index])  # Imprime cada cor da tupla usando um loop for com índices

for c in cor:
    print(c)  # Imprime cada cor da tupla usando um loop for direto sobre os elementos

for i in range(0, len(cor)):
    print(cor[i])  # Imprime cada cor da tupla usando um loop for com índices e a função len() para determinar o número de elementos
    
print(len(cor))  # Imprime o número de elementos na tupla (5)

type(cor)  # Imprime o tipo da variável cor (tuple)
print(type(cor))  # Imprime o tipo da variável cor (tuple) de forma mais clara


num = (10,20,55,40,60,7,8,60,10)
print(num.count(60))  # Imprime o número de vezes que o valor 60 aparece na tupla (2)
print(num.count(10))  # Imprime o número de vezes que o valor 10 aparece na tupla (2)
print(num.count(100)) # Imprime o número de vezes que o valor 100 aparece na tupla (0)
print(num.index(55))  # Imprime o índice do primeiro elemento com valor 55 (2)
print(num.index(60))  # Imprime o índice do primeiro elemento com valor 60 (4)
# print(num.index(100)) # Isso causará um erro, pois o valor 100 não está presente na tupla

ben = (1,)
print(type(ben))  # Imprime o tipo da variável ben (tuple), pois uma tupla com um único elemento deve ser definida com uma vírgula, como ben = (1,)

ben2 = (1)
print(type(ben2))  # Imprime o tipo da variável ben2 (int), pois sem a vírgula, Python interpreta como um inteiro, não uma tupla

pessoa = ("Bruno", 18, "professor")
nome, idade, profissao = pessoa  # Desempacotamento da tupla em variáveis individuais
print(nome)      # Imprime o nome (Bruno)
print(idade)     # Imprime a idade (18)
print(profissao) # Imprime a profissão (professor)

