'''
Fatiamento de strings
 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
i= inicio
f= fim
p= passo
Obs: a função len retornar a quantidade de caracteres da String
'''

variavel = 'Olá Mundo'
print(variavel[5]) # Mostra a 6 letra da variavel
# O primeiro inidice sempre é 0

print(variavel[-4]) # Neste caso irá mostrar o 5 elemento de trás pra frente


print(variavel[4:]) # Ele vai mostrar apenas da 5 letra em diante
print(variavel[4:7]) # Aqui ele vai ocultar todas as letras após a posição 7

print(variavel[:5]) # Neste caso vai mostrar apenas o inicio

print(len(variavel[4:7])) # Vai mostrar quantas letras tem no determinado fatiamento

#p = passo
print(variavel[0:9:2]) # No caso o passo ele vai pular 2 letras, e vai mostrar, vai pular duas letras e mostra

print(variavel[::-1]) # Neste caso ele vai inverter a String
