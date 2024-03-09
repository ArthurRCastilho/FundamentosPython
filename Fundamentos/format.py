# Outra forma de formatação
# Utlizando a função ".format()"

a = 'A'
b = 'B'
c = 1.111111
string = 'a= {} b= {} c= {}'
formato = string.format(a, b, c) # Será posicionado cada itens, de acordo com a ordem, ou seja a vem primeiro, então ele fica nas primeiras Chaves

formato2 = 'a= {} b= {} c= {:.3f}'.format(a, b, c)
formato2 = 'b= {1} a= {0} a= {0} b= {1} c= {2:.3f}'.format(a, b, c) # É possivel utilizar os indices também, n necessitando da ordem
formato3 = 'a= {} b= {nome2} c= {nome3:.5f}'.format(a, nome2=b, nome3=c) # Exite também o parametro nomeado, todos os parametro, após o que for nomeado, precisam ser nomeados

print(formato)
print(formato2)
print(formato3)