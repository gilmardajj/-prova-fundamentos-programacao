lista = [10,20,5,-3,0]

# print (lista [3])



# nome = ["rafael", "bruno", "alan", "ricardo", "leo"]

# print(nome [1])

# objeto = [10, "ras", 20, "raio", 30, "seis"]

# print(objeto [0])
# print (objeto)

print(range (5))# imprime o objeto range que representa os números de 0 a 4, usando a função range para criar uma sequência de números

print (range (len(lista)))# imprime o objeto range que representa os índices da lista, usando a função len para determinar o número de elementos

for i in range (len(lista)):# percorre os índices da lista usando a função range e len para determinar o número de elementos
    print(lista[i])# imprime cada elemento da lista usando um loop for e a função range para acessar os índices
lista[3] = 50# altera o valor na posição 3 da lista para 50
print(lista) # [10, 20, 5, 50, 0]

lista.append(35)# adiciona o valor 35 ao final da lista
lista.append(input("digite um numero para adicionar a lista: "))# adiciona o valor digitado pelo usuário ao final da lista
print(lista)# [10, 20, 5, 50, 0, 35, 'valor digitado pelo usuário']

lista.insert(1, 800) # insere o valor 800 na posição 1 da lista, deslocando os outros elementos para a direita
print(lista) # [10, 800, 20, 5, 50, 0, 35, 'valor digitado pelo usuário']

lista.insert(200, -5) # insere o valor -5 na posição 200 da lista, deslocando os outros elementos para a direita
print(lista) # [10, 800, 20, 5, 50, 0, 35, 'valor digitado pelo usuário', -5]

lista.remove(20) # remove o valor 20 da lista
print(lista) # [10, 800, 5, 50, 0, 35, 'valor digitado pelo usuário', -5]

lista.pop(2) # remove o elemento na posição 2 da lista, que é o valor 5
print(lista) # [10, 800, 50, 0, 35, 'valor digitado pelo usuário', -5]
print(lista[2]) # 50

lista.max() # retorna o maior valor da lista, que é 800
print(lista.max()) # 800

lista.min() # retorna o menor valor da lista, que é -5
print(lista.min()) # -5

lista.sort() # ordena os elementos da lista em ordem crescente
print(lista) # [-5, 0, 10, 35, 50, 800, 'valor digitado pelo usuário']

lista.sort(reverse=True) # ordena os elementos da lista em ordem decrescente
print(lista) # ['valor digitado pelo usuário', 800, 50, 35, 10, 0, -5]

lista.clear() # remove todos os elementos da lista, deixando-a vazia
print(lista) # []

lista.sum() # retorna a soma de todos os elementos da lista, que é 0
print(lista.sum()) # 0

lista.count(10) # conta quantas vezes o valor 10 aparece na lista, que é 0
print(lista.count(10)) # 0

lista.index(50) # retorna o índice da primeira ocorrência do valor 50 na lista, que é 2
print(lista.index(50)) # 2

lista.reverse() # inverte a ordem dos elementos da lista
print(lista) # [50, 35, 10, 0, -5]

lista.copy() # retorna uma cópia da lista, que é [50, 35, 10, 0, -5]
print(lista.copy()) # [50, 35, 10, 0, -5

lista.len() # retorna o número de elementos da lista, que é 5
print(lista.len()) # 5

