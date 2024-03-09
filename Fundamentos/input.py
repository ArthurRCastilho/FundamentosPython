nome = input('Qual o seu nome? ')
idade = int(input('Quantos anos você tem? ')) # Input sempre retorna uma String, portnato é necessário converter para int, colocando o input entre parenteses de int
idade_mais_10 = idade + 10

print(f'O seu nome é {nome} e você tem {idade} anos')
print(idade_mais_10)