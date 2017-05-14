# -*- coding: utf-8 -*-
"Command line application to generate start strings"

__version__ = "0.1.0"

import sys
from . import parse

# TODO
# instalacao com pip (local primeiro)
# deve ter as opcoes: -v, -h
# https://gehrcke.de/2014/02/distributing-a-python-command-line-application/
#  https://packaging.python.org/
#  https://docs.djangoproject.com/en/1.10/intro/reusable-apps/
#  http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
#  https://packaging.python.org/distributing/
# https://packaging.python.org/distributing/#uploading-your-project-to-pypi
# postar projeto no pip para outras pessoas usarem

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
