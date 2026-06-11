import random

# Gera 1000 inteiros aleatórios entre 1 e 1000
aleatorios = [random.randint(1, 1000) for _ in range(1000)]

print("maior", max(aleatorios))
print("menor", min(aleatorios))
print("tamanho", len(aleatorios))
print("soma", sum(aleatorios))

media = sum(aleatorios) / len(aleatorios)
print("Média dos números:", round(media, 2))  # round(..., 2) arredonda para 2 casas decimais

# Essa linha de código é uma das formas mais poderosas e usadas em Python. Ela se chama List Comprehension (Compreensão de Lista) 
# e serve para criar listas de forma rápida em apenas uma linha.Para entender como ela funciona, imagine que ela faz exatamente 
# o mesmo que este bloco de código tradicional:                      
# pythonaleatorios = []                # 1. Cria uma lista vazia
# for _ in range(1000):                # 2. Repete 1000 vezes
#     numero = random.randint(1, 1000) # 3. Sorteia um número de 1 a 1000
#     aleatorios.append(numero)        # 4. Adiciona o número no final da lista

#Divisão parte por parte:[ ... ] (Os colchetes externos)Dizem ao Python: "Tudo o que acontecer aqui dentro vai virar os elementos de uma nova lista".random.randint(1, 1000)É a ação que gera o valor. A função randint(1, 1000) escolhe um número inteiro aleatório entre 1 e 1000 (inclusive).for _ in range(1000)É o laço de repetição (loop) que dita quantas vezes a ação vai acontecer.range(1000) cria uma sequência de 1000 passos (do 0 ao 999).O underline _ é usado como o nome da variável do loop. Em Python, usamos o _ quando a variável do for não importa dentro do bloco (só queremos que o loop se repita 1000 vezes, não precisamos usar o número do passo atual).💡 Resumo do processo:O Python lê o código da direita para a esquerda: ele repete o loop 1000 vezes e, em cada repetição, roda o random.randint(1, 1000) e joga o resultado direto dentro da lista aleatorios.