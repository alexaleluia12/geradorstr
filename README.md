
entre "" serao sempre fixos
os parametros dinamicos vao aparecer na ordem que foram criados
saida no stdout


geradorstr "INSERT INTO PRODUTO VALUES (" parametros_dinamicos ... -q N
eg: geradorstr "INSERT INTO PRODUTO VALUES (NULL, " INT "," PRODUTO ", " PALAVRA ");" 8

N quantidade de linhas que serao geras
caso nao for especificado o inicio e fim serao sequenciais


== parametros dinamicos ==
(a,b,c) == escolha a a

INT
INT(inicio:fim)

FLOAT
FLOAT(inicio:fim)

NOME

PRODUTO

PALAVRA
PALAVRA(n)
