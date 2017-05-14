help="""String inteligente: feito para gerar uma sequência de linhas com partes fixas
e outras dinâmicas.
Ex: insert sql.

Entre "" serão sempre fixos.
Os parâmetros dinâmicos vão aparecer na ordem que foram criados.
Saída no stdout.

geradorstr "INSERT INTO PRODUTO VALUES (" parametros ... N
ex: geradorstr "INSERT INTO PRODUTO VALUES (NULL, " INT "," PRODUTO ", " PALAVRA ");" 8

N: quantidade de linhas que serão geradas (OBRIGATORIO)
caso não for especificado o início e fim serão sequenciais

== paramêtros ==

-v --verson (versão do geradorstr)
-h --help (ajuda)

INT                    # sequencial, comeca de um
INT{inicio:fim}        # randomico entre inicio e fim

FLOAT                  # sequencial, comeca de um
FLOAT{inicio:fim}      # randomico entre inicio e fim

NOME                   # nome de pessoa aleatorio

PRODUTO                # nome de produto aleatorio

PALAVRA                # palavra aleatoria
PALAVRA{n}             # n palavras aletorias sepadas por espaco

== exemplos ==
$ geradorstr "tenho " INT " " PALAVRA ' que valem ' INT{5:10} 5
$ geradorstr "INSER INT PRODUTOS VALUES (NULL, " PRODUTO ", " PALAVRA{2} ", " FLOAT{100:200} " )" 3
$ geradorstr altura ' + ' INT 10

Como instalar:

$ pip install geradorstr
"""

version="0.1.0"