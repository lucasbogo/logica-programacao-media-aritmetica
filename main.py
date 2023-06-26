# Contrua um algoritmo que calcule a média aritmética entre quatro notas bimestrais quaisquer fornecidas pelo aluno (usuário)
# Dados de entrada: 4 notas bimestrais (N1, N2, N3, N4)
# Dado de saída: média aritmética (MA)

# O que é média aritmética?
# Resposta: a soma de todos os valores dividido pela quantidade de valores

# Declaração de variáveis
N1 = 0
N2 = 0
N3 = 0
N4 = 0
MA = 0

# Entrada de dados
N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

# Processamento
MA = (N1 + N2 + N3 + N4) / 4

# Saída de dados

print("A média aritmética é: ", MA)