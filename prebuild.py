
import os
from geradorstr import funcoesauxiliares

with open('geradorstr' + os.path.sep + 'metainfo.py', 'w') as f:
    conteudo = funcoesauxiliares.get_readme()
    conteudo = 'help="""' + conteudo + '"""'
    f.write(conteudo)
    f.write("\n\n")

    versao = 'version="' + funcoesauxiliares.get_version() + '"'
    f.write(versao)


with open('README.md', 'w') as f:
    conteudo = funcoesauxiliares.get_readme()
    conteudo = '```text\n' + conteudo + '\n```'
    f.write(conteudo)
