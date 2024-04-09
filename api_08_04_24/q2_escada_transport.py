import math

# 2. [q2_escada_transport] O aumento ou perda de peso, de forma
# simplificada, é um o resultado da balança entre superávit ou déficit
#calórico. Se consumir mais do que precisa, aumenta o peso, caso
#contrário diminui ou mantém.
#De acordo com a OMS, um homem adulto em média precisa
#consumir apenas 2400 calorias/dia para manter o peso atual. Já
#as mulheres ficam em 2000 calorias. Ou seja, esse é o valor que
#gastamos em atividades do dia a dia, normais. Já para perder 1kg
#de peso é necessário o gasto calórico excedente de 7000 calorias.
#Na academia, temos uma série de exercícios do tipo aeróbico,
#dentre eles o Transport e Simulador de Escada. No Transport, um
#homem gasta em média 100 calorias a cada 5 min, já uma mulher
#a cada 6 min. E na escada, um homem gasta 100 calorias a cada
#7 minutos e a mulher a cada 8 minutos.
#Considerando as informações acima como verdade (informações
#hipotéticas), e que o ritmo alimentar permanecerá o mesmo.
#Faça um programa para auxiliar na perda de peso de homens e
#mulheres adultos. O objetivo é, de acordo com a situação atual
#(peso atual, se homem ou mulher, quantos quilos quer perder,
#quantos dias por semana irá fazer atividade física, e quanto tempo
#por dia irá treinar). Pergunte ainda qual proporção (%) de tempo
#alocada para o Transport, e calcule a contrapartida de Escada (os
#dois serão 100%).
#Seu objetivo, ao final, é informar em quantas semanas o usuário
#alcançará o objeto desejado, bem como indicar para cada dia de
#atividade física, quantos minutos de escada e quantos de
#Transport ele deverá seguir (todos os dias são iguais). Faça as
#validações adequadas.

peso = float(input('Informe seu peso atual: '))
sexo = str(input('Sexo (M - Masc. F - Feminino) '))

calorias_transport_min = 20 if sexo.lower() == 'm' else  16.66667
calorias_escada_min = 14.2857142 if sexo.lower() == 'm' else 12.5

metakilos = float(input('Quantos kilos deseja perder? '))
meta = metakilos * 9400 if sexo.lower() == 'm' else 9000


dias = int(input('Quantos dias por semana de treino? '))
tempo = int(input('Quantos minutos por treino? '))

pct_transport = float(input('Quanto (%) de tempo para Transport? '))
numerico_transport = pct_transport/100
pct_escada = 100-pct_transport
numerico_escada = pct_escada/100

mins_transport_dia = math.floor(numerico_transport*tempo)
mins_escada_dia = math.floor(numerico_escada*tempo)
dias_necess = 0

cals_dia = calorias_escada_min * mins_escada_dia + calorias_transport_min * calorias_transport_min

while meta > 0:
    meta -= cals_dia
    dias_necess += 1

semanas = math.ceil(dias_necess/dias)

print(f'''
========= RESULTADO ========
Sexo                            : {sexo}
Quantidade de kilos             : {peso} kgs
Qtd. de kilos que quer perder   : {metakilos} kgs
Semanas necessárias de treino   : {semanas} semanas
Minutos diários de ESCADA       : {mins_escada_dia}mins necessarios
Minutos diários de TRANSPORT    : {mins_transport_dia}mins necessarios
''')

    