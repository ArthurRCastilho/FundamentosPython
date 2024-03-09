def calculo_IMC(altura, peso):
    imc = peso / altura ** 2
    return imc

nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Digite seu peso (em Kgs): '))

meu_imc = calculo_IMC(altura, peso)

print(' ')
print(f"Olá {nome} seu IMC é: {meu_imc}")
print(f'Peso: {peso};')
print(f'Altura: {altura}.')
