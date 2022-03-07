#Desafio de programação CAPGEMINI 02
#Questão 03
#Autor: Douglas Almeida Carneiro

import math

def encriptacaoTexto(texto: str) -> str:

    if type(texto) != str:
        raise TypeError("Parâmetro 'texto' deve ser string")

    if len(texto) == 0:
        raise ValueError("Parâmetro 'texto' não pode ser uma string vazia")
    #Remove os espaços do texto
    textoTratado = texto.replace(" ", '')
    tamTexto = len(textoTratado)
    raizTamTexto = math.sqrt(tamTexto)
    linha = math.ceil(raizTamTexto)
    #Se a parte decimal da raiz quadrada for menor que 0.5, então a coluna pode ser menor que a linha em uma unidade que já é suficiente para alocar o textoTratado no grid. Caso seja maior que 0.5, linha e coluna são iguais. 
    coluna = round(raizTamTexto) 
    
    grid = [['']*coluna for i in range(linha) ]
    i = 0
    j = 0
    #Preenche o grid da esquerda para a direita e de cima para baixo com os caracteres do texto tratado
    for l in textoTratado:
        grid[i][j] = l
        if (j+1 < coluna):
            j += 1
        else:
            j = 0
            i += 1

    textoEncrip = ''
    #Monta o texto encriptado com os elementos do grid, percorrendo-o de cima para baixo e da esquerda para a direita
    for j in range(coluna):
        for i in range(linha):
            textoEncrip += grid[i][j]
        else:
            #Terminado esse for significa que uma coluna foi pecorrida, então um espaço é adicionado ao texto encriptado
            textoEncrip += ' '
    #Remove o espaço adicionado no final
    textoEncrip = textoEncrip.strip()

    return textoEncrip
    


if __name__ == '__main__':

    texto = input("Digite o texto a ser encriptado: ")
    
    rslt = encriptacaoTexto(texto)
    print(f"O texto encriptado é: \n{rslt}")
