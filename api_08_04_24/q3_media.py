def calcular_conceito(media):
    if media <= 2:
        return 'Péssimo'
    elif media <= 4:
        return 'Ruim'
    elif media <= 7:
        return 'Regular'
    elif media <= 8:
        return 'Bom'
    elif media <= 10:
        return 'Excelente'


def main():
    maior_nota = 0
    menor_nota = 99999999999
    soma_geral = 0
    homens = 0
    mulheres = 0
    somatorio_homens = 0
    somatorio_mulheres = 0
    count = 1

    sexo = 'm'
    while sexo == 'm' or sexo == 'f':
        print(f'===== ALUNO {count} =====')
        sexo = str(input('Sexo (m - masculino; f - feminino) '))
        if sexo == 'm' or sexo == 'f':
            if sexo == 'm':
                homens += 1
                nota = float(input('Nota: '))
                somatorio_homens+=nota
                if nota < menor_nota:
                    menor_nota = nota
                if nota > maior_nota:
                    maior_nota = nota
                soma_geral+=nota

            else:
                mulheres += 1
                nota = float(input('Nota: '))
                somatorio_mulheres+=nota
                if nota < menor_nota:
                    menor_nota = nota
                if nota > maior_nota:
                    maior_nota = nota
                soma_geral+=nota

            count+=1 
    
    mediageral = soma_geral/(homens+mulheres)
    media_mulheres = somatorio_mulheres/mulheres
    media_homens = somatorio_homens/homens
    desempenho_turma = calcular_conceito(mediageral)
    desempenho_homens = calcular_conceito(media_homens)
    desempenho_mulheres = calcular_conceito(media_mulheres)

    print(f'''
========= RESULTADO =========
Homens             : {homens}
Mulheres           : {mulheres}
Maior Nota Geral   : {maior_nota:.2f}
Menor Nota Geral   : {menor_nota:.2f}
Média Geral        : {mediageral:.2f}
Desempenho Turma   : {desempenho_turma} >>> {((soma_geral/(homens+mulheres))*10):.2f}%
Desempenho Homens  : {desempenho_homens} >>> {((somatorio_homens/homens)*10):.2f}%
Desempenho Mulheres: {desempenho_mulheres} >>> {((somatorio_mulheres/mulheres)*10):.2f}%
''')



main()