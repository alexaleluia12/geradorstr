
import re
import os
import random


def nrandom(lst, qnt=1):
    """
    lst -> list de string
    qnt -> quantidade de palavras na saida
    Retorna qnt elementos aletario de lst separados por espaco
    """
    saida = ""
    qnt -= 1
    for i in range(qnt):
        saida += random.choice(lst) + " "

    # para nao ficar espaco na ultima palavra
    saida += random.choice(lst)
    return saida


def get_version():
    version = re.search(
        '^__version__\s*=\s*"(.*)"',
        open('geradorstr'+os.path.sep+'geradorstr.py').read(),
        re.M
        ).group(1)
    return version


def get_readme():
    with open('README.rst', 'rb') as f:
        conteudo = f.read().decode('utf-8')

    return conteudo
