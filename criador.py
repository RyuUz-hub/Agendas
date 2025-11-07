from random import choice
from dados import *
from analisador import*

def horario(miranha='n', freela='n', trio='n', circo='n'):
    if trio == 's': # Fará um trio aleatório
        chars = fixos.copy()
        chars.pop('andreia')
        primeiro = choice(list(chars.keys()))
        chars.pop(primeiro)
        return f'{choice(trios)} ({primeiro.capitalize()}, {choice(list(chars.keys())).capitalize()}, Andreia)'
    if freela == 's': # Fará um freela aleatório
        return f'{choice(freelas)} '
    if miranha == 's': # Fará um horário com miranha e princesa
        return f'Homem-Aranha e {choice(princesas).capitalize()} (Abner, '
    elif circo != 'n':
        return str(choice(circos))
    
    # Fará uma dupla aleatória
    chars = fixos.copy()
    if choice([True, False]):
        first = choice(list(chars.keys())) # Escolhe pessoa1
        first_c = choice(chars[first]) # Pessoa1 char
        chars.pop(first) # Retira a pessoa escolhida da lista
        second = choice(list(chars.keys())) # Escolhe a segunda pessoa
        try:
            chars[second].remove(first_c)
        except:
            None
        second_c = choice(fixos[second]) # Escolhe um personagem da pessoa
        chars_f = f'{first_c.capitalize()} e {second_c.capitalize()} ({first.capitalize()}, {second.capitalize()})'
        return chars_f

    chars.pop('andreia')
    chars_f = f'{choice(duplas)} ({choice(list(chars.keys())).capitalize()}, Andreia)'

    return chars_f
    

def criar_dia(dia: str , folga=''):
    quant = choice([3, 4, 4])
    miranha = choice([1, 2])


    while True:
        errado = 0
        diaria = [f'19h às 20h {horario()}\n']
        if dia.lower() == 'paradao':
            if miranha == 1:
                diaria.append(f'20h às 21h {horario(miranha='s')}\n')
                diaria.append(f'21h às 22h {horario(trio='s')}\n')
            if miranha == 2:
                diaria.append(f'20h às 21h {horario(trio='s')}\n')
                diaria.append(f'21h às 22h {horario(miranha='s')}\n')
        
        elif quant == 3:
            if miranha == 1:
                diaria.append(f'20h às 21h {horario(miranha='s')}\n')
                diaria.append(f'21h às 22h {horario(trio='s')}\n')
                diaria.append(f'{choice(horarios2)} {choice([horario(freela='s'), horario(circo='s')])}\n')
                diaria.sort()
            if miranha == 2:
                diaria.append(f'20h às 21h {horario(trio='s')}\n')
                diaria.append(f'21h às 22h {horario(miranha='s')}\n')
                diaria.append(f'{choice(horarios2)} {choice([horario(freela='s'), horario(circo='s')])}\n')
                diaria.sort()

        elif quant == 4:
            horinhas = horarios[:]
            for horas in horinhas:
                diaria.append(f'{horas} {(choice([horario(miranha='s'), horario(freela='s'), horario(trio='s'), horario(circo='s')]))}\n')
            diaria.sort()
        
        diaria.insert(0, f'{dia.upper()}\n\n')
        diaria.append(f'22h às 23h {horario()}\n\n')
        diaria = ''.join(diaria)
        diaria.strip()


        for nomes in fixos:
            if diaria.count(nomes.capitalize()) != 2:
                errado = 1
                break
        for pers in pers_fixos:
            if diaria.count(pers) > 1:
                errado = 1
                break
        for frees in personagens:
            if diaria.count(frees) > 1:
                errado = 1
                break
        if unidecode(diaria.lower()).count('circo') != 1:
            errado = 1
        if dia == 'domingo':
            diaria = diaria.splitlines()[:-1]
            diaria = '\n'.join(diaria)
        if errado != 1:
            break
    return diaria