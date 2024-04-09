import random

def gerar_senha(num_digitos):
    count = 1
    digito = random.randint(1,9)
    ultimo = digito
    senha = f'{ultimo}'
    while count <= num_digitos:
        digito = random.randint(1,9)
        if digito != ultimo and digito != ultimo + 1 and digito != ultimo-1:
            senha += f'{digito}'
            ultimo = digito
            count += 1

    return senha


def main():
    num_digitos = int(input('Quantos digitos possui a senha? '))
    senha = gerar_senha(num_digitos)
    print(f'A sua senha é {senha}')
    satisfeito = int(input('''
Você está satisfeito com essa senha?
1 - SIM
2 - NAO                   
'''))
    while satisfeito == 2:
        senha = gerar_senha(num_digitos)
        print(f'A sua senha é {senha}')
        satisfeito = int(input('''
Você está satisfeito com essa senha?
1 - SIM
2 - NAO
'''))  

main()