import re
import random


import funcoesauxiliares
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
# re.match(r'int(\\(\d+:\d+\\))|^int$', 'intfoijfe')
# espressao regular com nome de grupo
# r'^int(\((?P<inicio>\d+):(?P<fim>\d+)\))?$'
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
meustipos = [
    re.compile(r'^(?P<principal>int)(\{(?P<inicio>\d+):(?P<fim>\d+)\})?$'),
    re.compile(r'^(?P<principal>float)(\{(?P<inicio>\d+):(?P<fim>\d+)\})?$'),
    re.compile(r'^(?P<principal>nome)$'),
    re.compile(r'^(?P<principal>produto)$'),
    re.compile(r'^(?P<principal>palavra)(\{(?P<qnt>\d+)\})?$')
]

lst_funcoes = {
    'int': random.randint,
    'float': random.uniform,
    'nome': random.choice,
    'produto': random.choice,
    'palavra': funcoesauxiliares.nrandom
}
correspondencia = {'int': int, 'float': float, 'nome': str}
nomes = ['Alex', 'Junior', 'Jose', 'Carlos', 'Carolina', 'Mariana', 'Fernanda',
         'Jaqueline', 'Andre', 'Lucas', 'Pedro', 'Juliano', 'Monteiro',
         'Rafael', 'Giovani', 'Bruna',  'Bruno', 'Vitoria', 'Jenifer',
         'Maria', 'Leticia', 'Patricia', 'Paloma', 'Ronaldo', 'Gilberto',
         'Lunciano', 'Ana', 'Aline', 'Jessica']
produtos = ['copo', 'carteira', 'mesa', 'lapis', 'janela', 'monitor', 'tinta',
            'livro', 'caneta', 'cariola', 'tigela', 'controle', 'tetergente',
            'pneu', 'banco', 'chave', 'guarda roupa', 'lampada', 'alicate',
            'pia', 'tenis', 'sandalia', 'blusa', 'camiseta', 'celular']
palavras = ['Lorem', 'Ipsum', 'texto', 'modelo', 'empresas', 'vindo', 'usado',
            'estas', 'desde', 'ano', 'quando', 'misturou', 'caracteres',
            'criar', 'livro', 'sobreviveu', 'decadas', 'altou tipografia',
            'mater', 'essencialmente', 'inalterada', 'popularizada', 'folha',
            'continham', 'passagens', 'mais', 'menos', 'soma', 'subtracao',
            'valores', 'recentemente', 'programas', 'incluem']


conjunto_string = {'nome': nomes, 'produto': produtos, 'palavra': palavras}
tipos_string = ['nome', 'produto', 'palavra']


class Dinamico:
    pass


class Estatico:
    pass


class Sequencia:
    def __init__(self, ordem, quantidade):
        self.ordem = ordem
        self.quantidade = quantidade


class Elemento:
    def __init__(self, tipo, valor=None, inicio=0, fim=0, nstring=1):
        self.tipo = tipo
        self.valor = valor
        self.inicio = inicio
        self.fim = fim

        if self.tipo is Dinamico:
            fn = lst_funcoes[valor]

            if self.valor not in tipos_string:
                # fn None vai saber que o elemento eh sequencial e nao existe
                # funcao especial
                fn = lst_funcoes[valor] if inicio and fim else None
                self.valor = correspondencia[valor]
                #  precisa fz a conversao para o tipo correto
                self.get_valor = self._closure(
                    self.valor(self.inicio), self.valor(self.fim),  fn
                )
            else:  # variates do tipo string
                self.valor = int  # para nao dar conflito em sequencial()
                self.get_valor = self._closure(
                    fn=fn, tipo=valor, nstring=nstring
                )

        else:
            self.get_valor = self._normal

    def _closure(self, inicio=0, fim=0, fn=None, tipo=None, nstring=1):
        # falta por a restircao do intervalor, e string (complicaod)
        contador = 0
        incrementador = self.valor(1)

        def sequencial():
            nonlocal contador
            contador += incrementador
            return str(contador)

        def intervalo_aleatorio():
            return str(fn(inicio, fim))

        def para_string(tipo, quantidade):
            def interno():
                return fn(conjunto_string[tipo], qnt=quantidade)
            return interno

        if inicio and fim and fn:
            return intervalo_aleatorio
        elif fn:
            return para_string(tipo, nstring)
        else:
            return sequencial

    def _normal(self):
        return self.valor

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "Elemento({}, {})".format(self.tipo, self.valor)


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
        match_re = tipo_aceitavel(tipo_futuro)
        if match_re:
            # elemento dinamico
            todos_elementos = match_re.groupdict()
            tmpv = todos_elementos.get('inicio', None)
            inicio = tmpv if tmpv else 0

            tmpv = todos_elementos.get('fim', None)
            fim = tmpv if tmpv else 0

            tmpv = todos_elementos.get('qnt', None)
            strqnt = int(tmpv) if tmpv else 1

            elemento = Elemento(
                Dinamico, match_re.group('principal'), inicio, fim, strqnt)

        else:
            # elemento statico
            elemento = Elemento(Estatico, antigo)

        lst_sequencia.append(elemento)

    return Sequencia(lst_sequencia, quantidade)


def tipo_aceitavel(valor):
    for m in meustipos:
        tmp = m.match(valor)
        if tmp:
            return tmp

    return False  # nenhum tipo dinamico
