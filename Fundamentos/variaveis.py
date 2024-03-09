# Variáveis são usadas para salvar coisas na memoria do computador
# PEP8: inicie variáveis com letras minúscuas, no lugar de espaço coloque "_"
# Exemplo: 
esta_e_uma_variavel = True

# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável)
# Uso: nome_variavel = expressão

nome_completo = 'Arthur Rodrigues'
print(nome_completo) # é possivel printar o que está dentro da variavel

soma_dois_mais_dois = 2 + 2  #Se selecionar o nome da variavel aparecerá o valor literal
print(soma_dois_mais_dois) #Print de somas, sem estarem feitas

#Variaveis, são utilizadas para tornar o código mais legivel, e para evitar repetições de expressões

conversion = bool(' ')
print(f"A conversão será feita na variavel, e o resultado será impresso: {conversion}")

nome = 'Arthur'
idade = 17
maior_de_idade = idade>=18
print('Nome: ', nome, 'Idade: ', idade)
print('É maior? ', maior_de_idade)