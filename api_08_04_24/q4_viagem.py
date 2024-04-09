import math

#Peça ao
#usuário Origem, Destino, Valor em R$ no site e Valor em Milhas no
#Site. Apresente para ele o valor equivalente em R$ caso compre
#com Milhas Padrão, indicando o % em relação ao valor em R$.
#Faça o mesmo para Milhas Baratas. Ao final, indique para ele a
#melhor forma de compra dentre as 3 opções.

def main():
    origem = str(input('Origem: '))
    destino = str(input('Destino: '))
    valorRS = float(input(f'Valor em R$ da passagem de {origem} a {destino}: '))
    milhas = int(input(f'Valor em Milhas da passagem de {origem} a {destino}: '))
    valorMilhasBaratas = milhas*0.01450
    print(math.ceil(milhas/1000))
    valorMilhasComuns = milhas*0.070

    pct_rs = 1
    pct_mb = valorMilhasBaratas/valorRS
    pct_mc = valorMilhasComuns/valorRS

    if pct_rs <= pct_mb and pct_rs <= pct_mc:
        opcao = 'Valor do Site'
    elif pct_mb <= pct_rs and pct_mb <= pct_mc:
        opcao = 'Milhas Baratas'
    elif pct_mc <= pct_rs and pct_mc <= pct_mb:
        opcao = 'Milhas Comuns'

    print(f'''
=========== VIAGEM ============
Origem                  : {origem}
Destino                 : {destino}
Milhas necessárias      : {milhas}
Valor do Site           : {valorRS:.2f} (100%)
Valor em milhas comuns  : {valorMilhasComuns:.2f} ({(pct_mc*100):.2f})%
Valor em milhas baratas : {valorMilhasBaratas:.2f} ({(pct_mb*100):.2f})%

A opção mais econômica é: {opcao}
''')

main()