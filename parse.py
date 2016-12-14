import re

"""
(a,b,c)

INT
INT(inicio:fim)
int(n:m)

FLOAT
FLOAT(inicio:fim)

NOME

PRODUTO

PALAVRA
PALAVRA(n)
"""

# outros tipos meus, (nome, produto, palavra)
#re.match(r'int(\\(\d+:\d+\\))|^int$', 'intfoijfe')
# espressao regular com nome de grupo
#r'^int(\((?P<inicio>\d+):(?P<fim>\d+)\))?$'
"""
>>> k = re.compile(r'^int(\((?P<inicio>\d+):(?P<fim>\d+)\))?$')
>>> k.pattern
'^int(\\((?P<inicio>\\d+):(?P<fim>\\d+)\\))?$'
>>> k.match('int')
<_sre.SRE_Match object; span=(0, 3), match='int'>
>>> k.match('int(19:11)')
<_sre.SRE_Match object; span=(0, 10), match='int(19:11)'>
>>> a = k.match('int(19:11)')
>>> a.group('inicio')
'19'
>>> a.group('fim')
'11'
"""
mestipos = [
    re.compile(r'^int(\(\d+:\d+\))?$')
]
correspondencia = {'int': int, 'float': float}


class Dinamico:
    pass


class Estatico:
    pass


class Sequencia:
    def __init__(self, ordem, quantidade):
        self.ordem = ordem
        self.quantidade = quantidade


class Elemento:
    def __init__(self, tipo, valor=None, inicio=0, fim=0):
        self.tipo = tipo
        if self.tipo is Dinamico:
            assert valor is not None, "Nao pode ser None o valor de um elemento\
                dinamico"
            assert valor is float or valor is int, "Tipos invalidos"
        self.valor = valor
        self.inicio = inicio
        self.fim = fim

        if self.tipo is Dinamico:
            self.get_valor = self._closure()
        else:
            self.get_valor = self._normal


    def _closure(self):
        # falta por a restircao do intervalor, e string (complicaod)
        contador = 0
        incrementador = self.valor(1)

        def interno():
            nonlocal contador
            contador += incrementador
            return str(contador)
        return interno

    def _normal(self):
        return self.valor

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "Elemento({}, {})".format(self.tipo, self.valor)

# TODO
# inserir o controle de minimo e maximo


def parse(lst):
    # ['INSERT INTO PRODUTO VALUES (NULL, ', 'INT', ',', 'PRODUTO', ', ', 'PALAVRA', ');', '8']
    # lst = list()
    lst_sequencia = list()
    quantidade = int(lst[-1])
    lst.pop()
    for i in lst:
        # i = str(i)
        antigo = i
        tipo_futuro = i.lower()
        if tipo_futuro in correspondencia:
            # elemento dinamico
            elemento = Elemento(Dinamico, correspondencia[tipo_futuro])
        else:
            # elemento statico
            elemento = Elemento(Estatico, antigo)

        lst_sequencia.append(elemento)

    return Sequencia(lst_sequencia, quantidade)
