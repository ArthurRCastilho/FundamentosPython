# Precedência entre os operadores aritméticos

# 1- (n + n)  # Primeiro o que está entre parenteses
# 2 - ** # Após números elevados
# 3 - * / // % # após divisão, e multiplicação
# 4 - + -  # Por fim adição e subtração

conta_1 = 1 + 1 ** 5 + 5  # 7
conta_2 = (1 + 1) ** (5 + 5) # 1024

print(conta_1)
print(conta_2)