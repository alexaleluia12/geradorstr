# -*- coding: utf-8 -*-
"Command line application to generate smart strings"

__version__ = "0.1.0"


import sys
import os
from . import parse

# TODO
# fz (a,b,c)
# adicionar testes automatizados
#

"""
['INSERT INTO PRODUTO VALUES (NULL, ', 'INT', ',', 'PRODUTO', ', ', 'PALAVRA', ');', '8']

extrair == saber
- quantidade
- sequencia(fixo ou dinamico)
    - dinamico (intervalor)

== o vai ser dado ==
class Sequencia:
    quantide
    ordem [Elemento]

Elemento
    get_valor (
        vai retornar o valor que se espera do elemento, ele fica resposavel por
        saber se eh fixo ou dinamico e a ordem que deve ser gerada
        pra numero sequencia posso usar closure
    )

"""


def main():
    # print(sys.argv[1:])
    # return
    sequencia = parse.parse(sys.argv[1:])
    for i in range(sequencia.quantidade):
        tmp = [j.get_valor() for j in sequencia.ordem]
        print("".join(tmp))

if __name__ == '__main__':
    # rodar python3 geradorstr.py "INSERT INTO produto values (" INT ", " "ANY ELEMENTO" ", "  FLOAT ");" 5
    # esta funcionado nada :( estralho
    # python3 geradorstr.py "face myself " INT " :) " PALAVRA{3} ' ' INT{5:10} 5
    main()
