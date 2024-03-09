def calculo_IMC(altura, peso):
    imc = peso / altura ** 2
    return imc

nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Digite seu peso (em Kgs): '))

meu_imc = calculo_IMC(altura, peso)

print(' ')
print(f"Olá {nome} seu IMC é: {meu_imc:.3f}") # Este f antes das aspas é a formatação, permite você usar variaveis dentro da string, se elas estiverem entre Chaves {}
print(f'Peso: {peso:.2f}') # É possivel também limitar a quantidade de casas decimais, após a virgula
print(f'Altura: {altura}.')
