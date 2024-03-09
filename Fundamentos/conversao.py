#Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imjtáveis e primitivos:
# str, int, float, bool

print('1' + '1')
print('a' + 'b')
# print('1' + 1) # esta linha vai dar problema, pelo falo de que estamos tentando somar um tipo inteiro com um String

print(int('1'), type(int('1'))) # Neste caso houve a conversão do primeiro número, de String para número inteiro
print(int('1') + 1)
print(float("1")+1) # É possivel somar um número inteiro com float.
print(bool(' ')) # Para transformar em bool, tem algumas regrinhas, neste caso será True, mas depende do valor dentro
print(str(11) + 'e') # É possivel transformar um número em String
