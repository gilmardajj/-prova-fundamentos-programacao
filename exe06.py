#1 analise de vendas
#considere a tupla:
#vendas = (1500, 2300, 1800, 2900, 3200, 2100, 1700)
#faça um programa que:
#A) exiba a maior venda
#B) exiba a menor venda
#C) calcule a média das vendas
#D) exiba a quantidade de vendas acima da média

vendas = (1500, 2300, 1800, 2900, 3200, 2100, 1700) # Tupla com os valores das vendas
print("Maior venda:", max(vendas)) # Exibe a maior venda
print("Menor venda:", min(vendas)) # Exibe a menor venda
media_vendas = sum(vendas) / len(vendas) # Calcula a média das vendas
print("Média das vendas:", media_vendas) # Exibe a média das vendas
print("Quantidade de vendas acima da média:", len([v for v in vendas if v > media_vendas])) # Exibe a quantidade de vendas acima da média

# ## FORMATO TRADICIONAL (Longo)
# vendas_acima = []                # 1. Cria uma lista vazia
# for v in vendas:                 # 2. Passa por cada venda
#     if v > media_vendas:         # 3. Testa se é maior que a média
#         vendas_acima.append(v)   # 4. Guarda na lista se for maior

# print(len(vendas_acima))         # 5. Conta o total acumulado
# ## FORMATO COMPREENSÃO DE LISTA (Curto)
# vendas_acima = [v for v in vendas if v > media_vendas] # 1. Cria uma nova lista com os valores de vendas que são maiores que a média
# print(len(vendas_acima)) # 2. Conta o total acumulado na nova lista

vendas = (1500, 2300, 1800, 2900, 3200, 2100, 1700)

# Inicializa as variáveis usando o primeiro elemento da tupla
maior_venda = vendas[0]
menor_venda = vendas[0]
soma_vendas = 0
total_elementos = 0

# Primeiro laço: calcula maior, menor, soma e quantidade total
for venda in vendas:
    if venda > maior_venda:
        maior_venda = venda
        
    if venda < menor_venda:
        menor_venda = venda
        
    soma_vendas += venda
    total_elementos += 1

# Calcula a média manualmente
media_vendas = soma_vendas / total_elementos

# Segundo laço: conta quantas vendas estão acima da média calculada
vendas_acima_da_media = 0
for venda in vendas:
    if venda > media_vendas:
        vendas_acima_da_media += 1

# Exibe os resultados na tela
print("Maior venda:", maior_venda)
print("Menor venda:", menor_venda)
print("Média das vendas:", media_vendas)
print("Quantidade de vendas acima da média:", vendas_acima_da_media)


# O que mudou na lógica:
# 
# Maior e Menor: Começam valendo o primeiro valor (1500). 
# O laço for compara cada número subsequente, substituindo a variável se encontrar um valor maior ou menor.
# Soma e len(): A variável soma_vendas acumula os valores linha por linha, enquanto total_elementos funciona como um contador manual para substituir o len().Acima da média: Um segundo laço percorre a tupla novamente após a média já estar calculada, somando +1 toda vez que encontra uma venda maior que a média.