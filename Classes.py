from random import choice, randint
pizzas = ['Calabresa', 'Pepperoni', 'Banana', 'Chocolate', 'Cheddar', 'Catupiry', 'Margerita', 'Frango']

class mesa:
    def __init__(self, numero_id, quant_pessoas: int, rodizios=0, brinquedoteca=0):
        self.numero_id = numero_id
        self.quant_pessoas = quant_pessoas
        self.hora_entrada = f'{randint(18, 21)}h{(randint(0, 59)):0>2}'
        self.hora_saida = f'{(int(self.hora_entrada[:2])) + randint(1, 2)}h{(self.hora_entrada[-2:])}'


        valor = (6990 * rodizios) + (2000 * brinquedoteca)
        if valor == 0: valor += (3500*quant_pessoas)
        valor = f'R${valor}'[:(len(str(valor)))] + ',' + str(valor)[-2:]
        self.valor = valor

        self.pedidos = 0

    def pedir(self):
        self.pedidos += 1
        return f'Pedido de {choice(pizzas)} na mesa {self.numero_id}'
    
    @classmethod
    def criação_de_mesas(cls, mesas):
        novas_mesas = [cls(numero_id, quant_pessoas, rodizios, brinquedoteca) for numero_id, quant_pessoas, rodizios, brinquedoteca in mesas]
        return novas_mesas

    def __repr__(self):
        return f'<MESA: {self.numero_id}, quantidade de pessoas: {self.quant_pessoas}, valor gasto {self.valor} entradas às {self.hora_entrada} e saíram às {self.hora_saida}>'

# (f'000{randint(1, 99)}'[-4:], randint(1, 5), randint(0, 5), randint(0, 3))
mesa_a, mesa_b, mesa_c = mesa.criação_de_mesas([(f'000{randint(1, 999)}'[-4:], randint(1, 5), randint(0, 5), randint(0, 3)), (f'000{randint(1, 999)}'[-4:], randint(1, 5), randint(0, 5), randint(0, 3)), (f'000{randint(1, 999)}'[-4:], randint(1, 5), randint(0, 5), randint(0, 3))])
mesa0001 = mesa('0001', 6, 6, 2)
print(mesa0001)
print(mesa_a.pedidos)
print(mesa_b)
print(mesa_c)