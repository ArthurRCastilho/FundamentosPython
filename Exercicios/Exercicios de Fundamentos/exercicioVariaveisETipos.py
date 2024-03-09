nome = 'Arthur'
sobrenome = 'Rodrigues'
idade = 20
ano_nascimento = 2023 - idade
maior_de_idade = idade >= 18
altura_metros = 1.65

if (maior_de_idade == True):
    maior_de_idade = 'Sim'
elif (maior_de_idade == False):
    maior_de_idade = "Não"

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)
