#!/usr/bin/env python3

import sys

import parse

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
        vai ternoar o valor que se espera do elemento, ele fica resposavel por
        saber se eh fixo ou dinamico e a ordem que deve ser gerada
        pra numero sequencia posso usar closure
    )

"""

def closure():
    count = 0

    def tmp():
        nonlocal count
        count += 1
        return count

    return tmp


def main():
    sequencia = parse.parse(sys.argv[1:])
    for i in range(sequencia.quantidade):
        tmp = [j.get_valor() for j in sequencia.ordem]
        print("".join(tmp))




if __name__ == '__main__':
    # rodar python3 geradorstr.py "INSERT INTO produto values (" INT ", " "ANY ELEMENTO" ", "  FLOAT ");" 5
    main()
