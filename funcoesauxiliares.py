
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
