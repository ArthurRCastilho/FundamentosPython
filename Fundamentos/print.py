print("Apresentando 1 e dois argumentos em 1 mesmo print:") #Usada para exibir as coisas na tela
print("Print 1: ")
print(12) # Será apresentado 1 argumento, no caso um número inteiro
print(" ") #Quebra de linha

print("Print 2: ")
print(12, 34) #Será apresentado 2 números inteiros, serão apresentados com 1 espaço entre eles. (OBS: A virgula não é apresentada, apenas para diferenciar os dois valores.)
print(" ")

print("Print 3: ")
print(74, 4) #Além disso, entre um print e outro, sempre haverá uma quebra de linha.
print(" ")

print("Mudando o separador entre os argumentos: ")
print("Print 1: ")
print(12, 34, sep=" e ") #Por padrão o Python separa os dois argumentos com um espaço, porém se colocar sep= eu posso escolher separador.
print(" ")

print("Print 2: ")
print(12, 34, sep=" - ") #Por padrão o Python separa os dois argumentos com um espaço, porém se colocar sep= eu posso escolher separador.
print("")

print("Aqui serão utilizados a função 'end=' no print")
print("Print 1:")
print(44, 66, sep=" - ", end=' ##\n')
print("Percebe-se que eu adicionei duas '#' no final do print com o end= ")
print(" ")

#Tipos de quebras de linhas pra cada sistema
# \r\n -> CRLF
# \n -> LF