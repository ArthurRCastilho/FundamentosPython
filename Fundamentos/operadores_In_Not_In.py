# in = entre
# not in = não está entre

# Operadores in e not in
# Strings são iteráveis

# Em uma String você consegue navegar entre as strings
# Indice
# 0 1 2 3 4 5
# A R T H U R

nome = 'Arthur'
print(nome[2])  # Vai printar a letra 't'

print('r' in nome) # Neste caso vai checar se a letra 'r' está entre a variavel r, se sim, True, se não False

print('ur' not in nome) # Neste caso ele vai perguntar, se 'ur' NÃO está no nome, se não estiver True, se estiver, True