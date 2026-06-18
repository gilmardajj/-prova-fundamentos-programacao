#2 dada a tupla: numero = (5,2,8,2,9,2,5,7,8,5)
#crie um programa que:
#A) descubra todos os números que aparecem mais de uma vez.
#B) mostre quantas vezes cada um deles aparece.

#exemplo de saída

#5 aparece 3 vezes
#2 aparece 3 vezes
#8 aparece 2 vezes
numero = (5, 2, 8, 2, 9, 2, 5, 7, 8, 5)

# Lista auxiliar para rastrear os números que já foram exibidos
repetidos = []

# Percorre cada número da tupla
for num in numero:
    # Conta quantas vezes o número aparece na tupla
    quantidade = numero.count(num)
    
    # Se aparecer mais de uma vez e ainda não tiver sido exibido
    if quantidade > 1 and num not in repetidos:
        print(f"{num} aparece {quantidade} vezes")
        repetidos.append(num)

# Como o programa funciona:
# 
# numero.count(num): Essa função nativa do Python conta exatamente quantas vezes o número atual aparece dentro da tupla.
# 
# quantidade > 1: Garante o requisito A, filtrando apenas os elementos repetidos.
# 
# num not in repetidos: Impede que o mesmo número seja processado e exibido múltiplas vezes na tela.
# 
# repetidos.append(num): Registra o número após a exibição para que ele seja ignorado nos próximos passos do laço de repetição.


