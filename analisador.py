from dados import *
from unidecode import unidecode
from time import sleep

def contar(periodo: str, total=''):
    """Variável periodo: dia ou agenda completa
    Objetivo da Função: contar as horas dos membros da equipe em um determinado periodo"""
    pessoas_horas = {}
    if periodo == '' or periodo == None:
        print('Dia não encontrado.')
        return
    
    if total == 'diaria':
        for nome in fixos:
            pessoas_horas[nome] = (unidecode(periodo.lower())).count(nome)
        return pessoas_horas


    pessoas_horas
    return pessoas_horas





def separar_dia(dia: str, agenda: str):
    """variável dia: str('segunda'... 'domingo')
    Variável agenda: str(agenda desejada)
    Objetivo da função: separar os dias da semana para melhor comparação futura"""
    string_dia = ''  # Variável em string para construir a tabela de nomes: horas
    dia = unidecode(dia.lower().strip()) # Substitui acentos
    agenda = unidecode(agenda.lower())
    its = 0

    if dia not in semanal:
        print('Dia inválido.')
        return None
    if dia not in agenda:
        print(dia, '\n\n', agenda)
        print('Dia não na agenda.')
        return None
    agenda = agenda.splitlines() # Separar a agenda em linha parar ler individualmente

    # Defini, para domingo, o final como última linha da agenda
    final = agenda[-1]
    if dia != 'domingo':
        # Defini o dia seguinte
        final = semanal[semanal.index(dia) + 1]

    while its < len(agenda):
        if dia in agenda[its]:
            # Achou a entrada 'dia' na linha 'its'
            try: # Try porque domingo dá erro no final
                while agenda[its].strip() != final:
                    string_dia += (f'{agenda[its]}\n')
                    its += 1
                if dia == 'domingo': # Adiciona a última linha no domingo
                    string_dia += agenda[-1]
                return string_dia  # Retorna uma string com nome: horas
            except:
                return string_dia
        its += 1
    print('Its ficou maior que len(agenda), não achou o inicio.')
    return None





def detalhar(pessoa: str, agenda='', diaria=''):
    """Variável pessoa: pessoa da equipe\n
    Variável agenda: agenda completa\n
    Objetivo da função: separar e atribui em dias os horários da pessoa para comparar com outra agenda"""
    pessoa = unidecode(pessoa.lower())
    agenda = unidecode(agenda.lower())
    diaria = unidecode(diaria.lower())
    if pessoa not in pessoas_horas or (agenda == '' and diaria == ''):
        print('Dados fornecidos incorretamente')
        return None
    
    if diaria != '':
        dicionario = {pessoa: []}
        for linha in diaria.splitlines(): # Leia as linhas do dia
            if pessoa in linha: # A pessoa está na linha?
                dicionario[pessoa].append(linha.split()[0])
        return dicionario

    # separar cada dia, e por cada dia, ler os horário da pessoa e colocar no seu respectivo dia
    dicionario = {pessoa: {'segunda': [], 'terca': [], 'quarta': [], 'quinta': [], 'sexta': [], 'sabado': [], 'domingo': []}}
    for dias in semanal: # No dia da semana
        dia = separar_dia(dias, agenda) # dia = string_dia
        if dia == None:
            continue
        for linha in dia.splitlines(): # Leia as linhas do dia
                if pessoa in linha: # A pessoa está na linha?
                    dicionario[pessoa][dias].append(linha.split()[0])
                if 'pocket' in linha:
                    resp = input(f'{str(pessoa).capitalize()} fez o pocket show de {linha.split()[-1]} no(a) {dias} S/N: ')
                    if resp.lower() == 's' or resp.lower() == 'sim':
                        dicionario[pessoa][dias].append(linha.split()[0])
    return dicionario




def validar(dicis: dict, periodo: str):
    """Objetivo da função: verificar as horas e retornar True ou False caso as horas colidam\n
    Variável dicis: dicionário feito pelo detalhamento\n
    Variável periodo: dia ou agenda completa\n
    """
    pessoa = str(list(dicis.keys())[0])
    periodo = unidecode(periodo.lower())
    dia = unidecode(periodo.splitlines()[0].lower().strip())
    if len(list(dicis.keys())) == 1:
        for c in range(len(dicis[pessoa])):
            if dicis[pessoa][c-1][:2] == dicis[pessoa][c][:2]:
                return False
            try:
                if '3' in dicis[pessoa][c] and int(dicis[pessoa][c][:2])+1 == int(dicis[pessoa][c+1][:2]):
                    return False
            except IndexError:
                False
        return True

    for dia in semanal:
        for c in range(len(dicis[pessoa][dia])):
            if dicis[pessoa][dia][c-1][:2] == dicis[pessoa][dia][c][:2]:
                return False
            try:
                if '3' in dicis[pessoa][dia][c] and int(dicis[pessoa][dia][c][:2])+1 == int(dicis[pessoa][dia][c+1][:2]):
                    return False
            except IndexError:
                False
    return True

            

# antecessora hora comparada com sucessora
# deve invalidar se os 2 caracteres da sucessora forem iguais à sucessora (21h, 21h30)
# if [ant][:2] == [suc][:2]:
    # return False

# deve invalidar se o antecessor tiver h30 e o seguinte não, sendo uma hora na frente (21h30, 22h)
# if '3' in [ant]:
    # if int([ant][:2])+1 == [suc][:2]:
        # return False


def completar(pessoa, rodizio, pizzagyn): # Formata o detalhar para ficar legível
    if pessoa not in pessoas_horas:
        return
    pessoa_horas_rd = detalhar(pessoa, rodizio) # Retorna o dicionário com as horas da pessoa em dias
    pessoa_horas_pg = detalhar(pessoa, pizzagyn)
    string_pessoa = ''

    for dias in pessoa_horas_rd[pessoa]: # 'dias' = dias da semana
        string_pessoa += f'{dias.capitalize()}: {pessoa_horas_rd[pessoa][dias]}, {pessoa_horas_pg[pessoa][dias]}\n'
    string_pessoa = string_pessoa.replace('[', '').replace(']', '').replace("'", '').replace(' , ', ' ').splitlines()

    for linha in string_pessoa:
        if linha.strip().endswith(','):
            string_pessoa[string_pessoa.index(linha)] = linha.strip().rstrip(',')
    
    final = string_pessoa[:]
    for linha in string_pessoa:
        if linha.endswith(' '):
            final.remove(linha)
    
    final = '\n'.join(final)
    return final

def contabilizar(periodo: str):
    diarias = 0
    horas_freelas = 0
    for pesso in fixos:
        diarias += int(unidecode(periodo.lower()).count(pesso))
    for fres in personagens:
        horas_freelas += int(unidecode(periodo.lower()).count(unidecode(fres.lower())))
    print(f'R${horas_freelas*100} em horas de freelance')
    horas_freelas += int(unidecode(periodo.lower()).count('pocket')) * 5
    diarias /= 2
    print(f'R${int(diarias) * 110} em diárias')
    print(f'R${horas_freelas*100} em total de freelancer com Pockets incluídos')