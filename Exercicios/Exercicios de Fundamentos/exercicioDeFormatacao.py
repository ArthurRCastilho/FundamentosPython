"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A útilma letra do seu nome é {letra}
Se nada for digitado em nome ou idade
    Exiba:
        "Desculpe, você deixou campos vazios"
"""

# Peça ao usuário digitar seu nome e idade

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# Se nome e idade forem digitados:
if nome and idade:
    # Seu nome é {nome}
    print(f"Seu nome é {nome}")
    # Seu nome invertido é {nome invertido}
    print(f"Seu nome invertido é {nome[::-1]}")
    # Seu nome contém (ou não) espaços
    if ' ' in nome:
        print("Seu nome contém espaço(s)")
    else:
        print("Seu nome NÃO contém espaços")
    # Seu nome tem {n} letras
    print(f"Seu nome tem {len(nome)} letras")
    # A primeira letra do seu nome é {letra}
    print(f"A primeira letra do seu nome é {nome[0]}")
    # A ultima letra do seu nome é {letra}
    print(f"A ultima letra do seu nome é {nome[-1]}")

# Se nada for digitado em nome ou idade
else:
    print("Desculpe, você deixou campos vazios")