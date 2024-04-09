def main():
    opcao = 9
    lista_str = ''
    total = 0
    cont_items = 1
    while opcao != 0:
        menu()
        opcao = int(input('> '))
        if opcao == 1:
            prod = str(input('Qual produto deseja adicionar? '))
            qto = str(input(f'Quanto de {prod} deseja adicionar? (ex.: 2Kg, 3L) '))
            valor = float(input(f'Quanto custa {qto} de {prod}?? '))
            total += valor
            lista_str += f'{cont_items}- {prod} ({qto})\t\t R${valor:.2f}\n'
            cont_items+=1

        elif opcao == 2:
            print(f'''
================================
{lista_str}================================
Total a Pagar:\t\t R${total:.2f}''')
            if total < 30:
                parcelas_juros = 6
                montante = total * (1+0.05)**parcelas_juros              
                print(f'À vista ou Pix:\t\t R${total:.2f}')
                print(f'Em 6x no cartão:\t R${montante:.2f}')
            elif total <100:
                parcelas_juros = 6
                montante = total * (1+0.05)**parcelas_juros              
                print(f'À vista ou Pix:\t\t R${total:.2f}')
                print(f'Em 3x no cartão:\t R${(total/3):.2f} (SEM JUROS)')
                print(f'Em 6x no cartão:\t R${montante:.2f} (COM JUROS)')
            else:
                parcelas_juros = 6
                montante = total * (1+0.05)**parcelas_juros              
                print(f'À vista ou Pix:\t\t R${total:.2f}')
                print(f'Em 5x no cartão:\t R${(total/5):.2f} (SEM JUROS)')
                print(f'Em 6x no cartão:\t R${montante:.2f} (COM JUROS)')
            input('\nAperte ENTER para voltar...')

        elif opcao == 0:
            print('Saindo...')
        else:
            print('Opção inválida!')



def menu():
    print('''
1 - Incluir Item
2 - Mostrar Lista
0 - Sair
          
O que deseja fazer?          
''')


main()