# DesafioCapgemini
Aqui estão relatadas as instruções de uso e demais detalhes acerca da implementaçao das questão do Desafio de Programação 02, uma das etapas do processo seletivo da Academia Técnica Capgemini 2022.

Além do Python 3, não é necessário instalar nenhum pacote extra.
Cada uma das questões resolvidas estão num arquivo diferente.

Cada teste unitário está num arquivo separado, respectivo à função que ele avalia.
Por convenção, o nome dos arquvos de teste são:
    "teste_<nome_do_modulo_testado>.py"

A estrutura dos arquivos ficaram assim:
  -mediana.py: Questão 01
  -diferenca.py: Questão 02
  -encriptacaoTexto.py: Questão 03
  -teste_mediana.py: Arquivo com testes unitários da função mediada.
  -teste_diferenca.py: Arquivo com testes unitários da função diferenca
  -teste_encriptacaoTexto.py: Arquivo com testes unitários da função encriptacaoTexto
  -SortingAlgorithm.py: Contém a função auxiliar que ordena de forma crescente um dado array.


Para executar diretamente algum dos scripts:
    -Rodar o seguinte comando:
        python3 <nome_do_arquivo.py>

Já para executar os testes unitários, há duas formas:
    -Executar o teste de apenas um dos scripts:
        python3 -m unittest <nome_do_arquivo_teste.py>
    -Executar todos os testes de uma vez (o Python busca automaticamente por eles):
        python3 -m unittest

Os comandos acima funcionam somente se o usuário tiver navegado até a pasta onde os arquivos estão.
Contudo, para que isso não seja necessário, pode ser passado o caminho completo do arquivo ao invés de apenas seu nome base.

O comando 'python3' funciona para sistemas operacionaos Unix.
O comando equivalente no Windows é 'py'

 
