from unidecode import unidecode
from random import choice

pessoas_horas = {'abner': 0, 'andreia': 0, 'nael': 0, 'pedro': 0, 'daniel': 0, 'flavio': 0, 'kety': 0, 'lara': 0, 'lister': 0, 'lorena': 0, 'taina': 0, 'yuri': 0, 'will': 0, 'angela': 0}

fixos = {'abner': ['Buzz', 'Super Pizza', 'Mickey', 'Donald', 'Stitch', 'Deadpool'], 'pedro': ['Buzz', 'Super Pizza', 'Mickey', 'Donald', 'Stitch', 'Miles Morales'], 'nael': ['Buzz', 'Sonic', 'Super Pizza', 'Mickey', 'Donald', 'Stitch'], 'andreia': ['Galinha Pintadinha']}

princesas = ['tinkerbell', 'cinderela', 'rapunzel', 'ariel']
freelas = ['Rapunzel, Flynn e Gothel', 'Jasmine, Aladdin e Gênio', 'Pocket Show: Branca de Neve', 'Pocket Show: Frozen']
personagens = ['Rapunzel', 'Flynn', 'Gothel', 'Cinderela', 'Príncipe', 'Ariel', 'Tinkerbell', 'Aladdin', 'Jasmine', 'Bela']
pers_fixos = ['Buzz', 'Super Pizza', 'Mickey', 'Donald', 'Stitch', 'Miles Morales', 'Deadpool', 'Galinha Pintadinha', 'Sonic']
circos = ['Apresentação Circo: Malabares', 'Apresentação Circo: Perna de Pau', 'Apresentação Circo: Balões', 'Apresentação Circo: Mágico']

semanal = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
horarios = ['20h às 21h', '20h30 às 21h30', '21h às 22h', '21h30 às 22h30']
horarios2 = ['20h30 às 21h30', '21h30 às 22h30']
duplas = ['Mickey e Minnie', 'Donald e Margarida', 'Stitch e Angel']
trios = ['PJ Masks', 'Mickey, Minnie e Donald', 'Mickey, Donald e Margarida']


semana_rd = """RODÍZIO E DIVERSÃO 

SEGUNDA

19h às 20h Buzz e galinha pintadinha (Pedro e Andréia)
20h às 21h Ariel, Sonic e homem aranha (Lara, Nael e Abner)
21h às 22h Stitch, Angel e super pizza (Abner, Andreia e Nael)
22h às 23h Tinkerbell e deadpool (Lara e Pedro)

TERÇA 

19h às 20h Stitch e Angel (Nael e Andreia)
20h às 21h Jasmine, Aladin e gênio (Lara, Abner e Pedro)
20:30 as 21:30 circo: Camilim Show (com escultura de balões)
21h às 22h homem aranha (Abner)
21:30 às 22:30 pj masks (Andréia, Pedro e Nael)
22h às 23h super pizza (Abner)

QUARTA 

19h às 20h galinha pintadinha e super pizza (Andréia e Nael)
20h às 21h pocket show: Frozen
21h às 22h homem aranha, miles Morales e Sonic (Abner, Pedro e Nael)
21:30 as 22:30 circo: Palhaço Juanito circo show
22h às 23h pj masks (Andréia Abner e Pedro)

QUINTA 

19h às 20h Stitch e Angel (Pedro e Andréia)
20h às 21h Cinderela e príncipe (Lorena e Flávio)
20:30 às 21:30 homem aranha (Pedro)
21h às 22h Jasmine Aladdin e gênio (Lara, Abner e Nael)
21:30 as 22:30 circo: show de malabares
22h às 23h Pj masks (Andréia, Nael e Abner)

SEXTA

19h às 20h mickey e Donald (Abner e Nael)
20h às 21h pocket show: Branca de neve
21h às 22h homem aranha e miles Morales (Abner e Pedro)
21h às 22h circo: show de bambolês
22h às 23h Buzz e Super pizza (Pedro e Nael)

SABADO

19h às 20h Stitch e Angel (Andréia e Pedro)
20h às 21h homem aranha e Sonic (Abner e Nael)
20:30 as 21:30 Pj masks  (Andréia, Pedro e Nael)
21h às 22h apresentação: Rapunzel, mamãe gothel e Flyn (Tainá, Maria e Lister)
21:30 as 22:30 circo: o equilibrista maluco, show de monociclo
22h às 23h Super pizza  (Abner)

DOMINGO  

19h às 20h Mickey e Minnie (Pedro e Andréia)
20h às 21h homem aranha e buzz (Abner e Nael)
20:30 as 21:30 pocket show Frozen
21h as 22h Stitch e Angel (Andréia e Abner)
21:30 as 22:30 circo: show da malevola e a bola mágica
22h as 23h Deadpool e super pizza (Pedro e Nael)"""

semana_pg = """Pizza
 
Terça 

20h as 21h Patrulha canina (Yuri e Daniel)
21h às 22h homem aranha e Mickey (Yuri e Daniel)

Quarta

19:30 às 20:30 homem de ferro (Yuri)
20h as 21h Barbie e homem aranha (Lorena e Daniel)
21h as 22h mickey e Minnie (Yuri e Daniel)

Quinta

19h as 20h Mickey e Minnie (Yuri e Tainá)
19:30 às 20:30 Jasmine, Gênio e Aladdin (Lara nael e Abner)
20:30 às 21:30 Ariel e homem aranha (Tainá e Daniel)
21h às 22h Homem de ferro e tchuchucao (Yuri e Daniel)

Sexta

19:30 às 20:30 Deadpool e Homem aranha e miles Morales (Pedro Yuri e Daniel)
20:30 às 21:30 Cinderela e príncipe (Tainá e Flávio)
21:30 as 22:30 homem de ferro e Mário (Yuri e Daniel)

Sábado

19:30 às 20:30 apresentação: Rapunzel, mamãe gothel e flyn (Tainá, Maria e Lister)
20h às 21h Moana e homem aranha (Kety e Daniel)
21h às 22h Patrulha canina (Kety e Daniel)"""

semana_criada = """SEGUNDA

19h às 20h Galinha pintadinha e Mickey (Andreia, Pedro)
20h às 21h PJ Masks (Nael, Abner, Andreia)
21h às 22h Homem-Aranha e Ariel (Abner, 
22h às 23h Buzz e Stitch (Nael, Pedro)

TERÇA

19h às 20h Sonic e Miles morales (Nael, Pedro)
20h às 21h Homem-Aranha e Cinderela (Abner,
21h às 22h PJ Masks (Nael, Abner, Andreia)
21h30 às 22h30 Rapunzel, Flynn e Gothel
22h às 23h Stitch e Angel (Pedro, Andreia)

QUARTA

19h às 20h Sonic e Deadpool (Nael, Pedro)
20h às 21h Homem-Aranha e Cinderela (Abner,
21h às 22h PJ Masks (Abner, Nael, Andreia)
21h30 às 22h30 Jasmine, Aladdin e Gênio
22h às 23h Mickey e Minnie (Pedro, Andreia)

QUINTA

19h às 20h Stitch e Angel (Nael, Andreia)
20h às 21h Homem-Aranha e Ariel (Abner,
20h30 às 21h30 Rapunzel, Flynn e Gothel
21h às 22h Mickey, Donald e Margarida (Pedro, Abner, Andreia)
22h às 23h Buzz e Miles morales (Nael, Pedro)

SEXTA

19h às 20h Miles morales e Sonic (Pedro, Nael)
20h às 21h Jasmine, Aladdin e Gênio
20h30 às 21h30 Pocket Show: Frozen
21h às 22h Homem-Aranha e Cinderela (Abner,
21h30 às 22h30 Mickey, Minnie e Donald (Abner, Nael, Andreia)
22h às 23h Deadpool e Galinha pintadinha (Pedro, Andreia)

SÁBADO

19h às 20h Stitch e Angel (Abner, Andreia)
20h às 21h Homem-Aranha e Tinkerbell (Abner,
20h30 às 21h30 Jasmine, Aladdin e Gênio
21h às 22h Rapunzel, Flynn e Gothel
21h30 às 22h30 Mickey, Donald e Margarida (Nael, Pedro, Andreia)
22h às 23h Deadpool e Super pizza (Pedro, Nael)

DOMINGO

19h às 20h Sonic e Donald (Nael, Abner)
20h às 21h PJ Masks (Nael, Pedro, Andreia)
20h30 às 21h30 Rapunzel e Flynn
21h às 22h Homem-Aranha e Tinkerbell (Abner,
22h às 23h Deadpool e Galinha pintadinha (Pedro, Andreia)"""

semana_criada = unidecode(semana_criada).lower()
semana_pg = unidecode(semana_pg).lower()
semana_rd = unidecode(semana_rd).lower()