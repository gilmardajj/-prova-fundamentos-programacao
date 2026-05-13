# O aluno deverá desenvolver um programa em Python que registre vendas de produtos e apresente um resumo final.

# Funcionalidades obrigatórias
# 4.1 Exibir menu inicial
# Valor: 1,0 ponto

# Ao iniciar o programa, deve aparecer um menu semelhante a este:

 
# === SISTEMA DE VENDAS ===

# 1 - Registrar venda
# 2 - Ver resumo parcial
# 3 - Encerrar sistema

# Escolha uma opção:
 
# O menu deve continuar sendo exibido até que o usuário escolha a opção 3.

# 4.2 Registrar venda
# Valor: 1,0 ponto

# Quando o usuário escolher a opção 1, o programa deverá solicitar:

 
# Nome do produto:
# Valor unitário:
# Quantidade:
 
# 4.3 Calcular valor Bruto
# Valor: 1,0 ponto

# Depois, deverá calcular o valor bruto da venda:

 
# valor_bruto = valor_unitario * quantidade
 
# Exemplo:

 
# Nome do produto: Camiseta
# Valor unitário: 50
# Quantidade: 3

# Valor bruto da venda: R$ 150.00
 
# 4.4 Aplicar desconto com estrutura condicional
# Valor: 1,5 pontos

# O programa deverá aplicar desconto conforme o valor bruto da venda:

# Valor bruto da venda	Desconto
# Menor que R$ 100,00	0%
# De R$ 100,00 até R$ 499,99	5%
# De R$ 500,00 até R$ 999,99	10%
# R$ 1.000,00 ou mais	15%
# O programa deverá mostrar:

 
# Desconto aplicado:
# Valor do desconto:
# Valor final da venda:
 
# Exemplo:

 
# Valor bruto da venda: R$ 600.00
# Desconto aplicado: 10%
# Valor do desconto: R$ 60.00
# Valor final da venda: R$ 540.00
 
 
 
# 4.5 Uso correto de repetição para manter o sistema ativo
# Valor: 1,0 ponto

# Deve-se estabelecer um critério de parada do sistema.
 
# 4.6 Acumular dados das vendas
# Valor: 1,5 ponto

# Durante a execução do programa, o sistema deverá acumular:

# quantidade total de vendas realizadas;
# valor total bruto vendido;
# valor total de descontos concedidos;
# valor total líquido vendido.
# Exemplo:

 
# Total de vendas realizadas: 4
# Total bruto vendido: R$ 2300.00
# Total de descontos concedidos: R$ 245.00
# Total líquido vendido: R$ 2055.00
 
# 4.7 Ver resumo parcial
# Valor: 1,0 ponto

# Quando o usuário escolher a opção 2, o programa deverá mostrar o resumo acumulado até o momento.

# Exemplo:

 
# === RESUMO PARCIAL ===

# Total de vendas realizadas: 2
# Total bruto vendido: R$ 700.00
# Total de descontos concedidos: R$ 60.00
# Total líquido vendido: R$ 640.00
 
# Caso nenhuma venda tenha sido registrada, o programa deverá exibir:

 
# Nenhuma venda registrada até o momento.
 
# 4.8 Encerrar sistema
# Valor: 0,5 ponto

# Quando o usuário escolher a opção 3, o programa deverá exibir o resumo final e encerrar.

# Exemplo:

 
# === RESUMO FINAL ===

# Total de vendas realizadas: 3
# Total bruto vendido: R$ 1500.00
# Total de descontos concedidos: R$ 160.00
# Total líquido vendido: R$ 1340.00

# Sistema encerrado.
 
# 5. Tratamento de opção inválida
# Valor: até 1,0 ponto

# Caso o usuário digite uma opção diferente de 1, 2 ou 3, o sistema deverá exibir:

 
# Opção inválida. Tente novamente.
 
# O menu deverá ser apresentado novamente.


# Inicialização dos Contadores ou aomuladores
total_vendas = 0
total_bruto = 0.0
total_descontos = 0.0
total_liquido = 0.0

while True:
    # Exibir menu inicial
    print("\n=== SISTEMA DE VENDAS ===")
    print("1 - Registrar venda")
    print("2 - Ver resumo parcial")
    print("3 - Encerrar sistema")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        # Registrar venda
        produto = input("Nome do produto: ")
        valor_unitario = float(input("Valor unitário: "))
        quantidade = int(input("Quantidade: "))

        # Calcular valor Bruto
        valor_bruto_venda = valor_unitario * quantidade
        print(f"\nValor bruto da venda: R$ {valor_bruto_venda:.2f}")

        # Aplicar desconto com estrutura condicional
        if valor_bruto_venda < 100:
            percentual = 0
        elif valor_bruto_venda < 500:
            percentual = 5
        elif valor_bruto_venda < 1000:
            percentual = 10
        else:
            percentual = 15

        valor_desconto = valor_bruto_venda * (percentual / 100)
        valor_final = valor_bruto_venda - valor_desconto
        print(f"Desconto aplicado: {percentual}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Valor final da venda: R$ {valor_final:.2f}")

        # Acumular de informações
        total_vendas += 1
        total_bruto += valor_bruto_venda
        total_descontos += valor_desconto
        total_liquido += valor_final

    elif opcao == '2':
        # Ver resumo parcial
        if total_vendas == 0:
            print("\nNenhuma venda registrada até o momento.")
        else:
            print("\n=== RESUMO PARCIAL ===")
            print(f"Total de vendas realizadas: {total_vendas}")
            print(f"Total bruto vendido: R$ {total_bruto:.2f}")
            print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
            print(f"Total líquido vendido: R$ {total_liquido:.2f}")

    