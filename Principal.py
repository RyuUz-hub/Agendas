from analisador import *
from criador import *


while True:
    agendah = ''
    for dias in semanal: # no dia da semana
        while True:
            errado = 0
            diaa = ''
            diaa = criar_dia(dias) # cria o dia
            for equipe in fixos:
                dici = detalhar(equipe, diaria=diaa)
                if validar(dici, diaa) == False:
                    errado = 1
            if errado == 1:
                continue
            break
        agendah += f'{diaa}\n'
    if agendah.count('Pocket') != 3:
        #print('resetou por pocket')
        continue
    if agendah.count('Aladdin') != 2:
        #print('resetou por aladdin')
        continue
    break

with open('agendatemp.txt', 'w', encoding='utf-8') as conteudo:
    conteudo.write(agendah)

#with open('agendatemp.txt', 'r', encoding='utf-8') as conteudo:
    #agendah = conteudo.read()

print(agendah)
pergunta = input('Deseja contabilizar as horas? ')
if pergunta == 'sim':
    contabilizar(agendah)