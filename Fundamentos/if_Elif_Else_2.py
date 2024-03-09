#if / elif     / else
#se / se não se / se não
condicao = 10 == 11
condicao2 = 11 == 11

# Sempre executa apenas uma condição de IF
# Começa com if, elif e encerra com else.
# Se colocar if dnv, é outra condição

if condicao:
    print('Falso')
elif condicao2:  # Elif é uma continuação do IF. Se caso for outro IF, ele pode ser executado mais de uma condição
    print ('Verdadeiro')
else:
    print('Este é o else')  # Aqui se encerra o primeiro if

if 10 == 10:
    print('verdadeiro if dois')
elif 11 == 10:
    print('Falso do if dois')
else:
    print('Else do if dois') # Com o else se encerra o IF dois

print('teste')  # Será executado após o if, mesmo se o if for verdadeiro ou não
