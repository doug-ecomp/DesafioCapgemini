#Desafio de programação CAPGEMINI 02
#Questão 02
#Autor: Douglas Almeida Carneiro

from SortingAlgorithm import quickSort
from typing import Union

def diferenca(arr: list, dif: Union[int,float]) -> int:
    """Calcula a quantidade de pares ordenados formados pelo produto cartesiano no conjunto de elementos de 'arr' cuja diferença absoluta seja igual a 'dif'.

    :param arr: Array com valores numéricos
    :dif: Diferenca buscada entre os pares ordenados formados pelos elementos de 'arr'
    :return: Quantidade de pares cuja diferença absoluta é 'dif'
    """

    #Lança exceção caso dif não seja um número
    if type(dif) not in [int, float]:
        raise TypeError("Parâmetro 'dif' deve ser um número")
    
    #Lança exceção caso 'dif' seja negativo
    if dif < 1:
        raise ValueError("Parâmetro 'dif' não pode ser um número negativo")

    #Lança exceção caso haja elementos não numéricos em arr
    for n in arr:
        if type(n) not in [int, float]:
            raise TypeError("Parâmetro 'arr' deve conter apenas valores numéricos") 
    
    #Lança exceção caso o array de entrada esteja vazio
    if len(arr) == 0:
        raise ValueError("Parâmetro 'arr' não pode ser vazio")
    
    #Ordena arr de forma crescente
    arrSorted = quickSort(arr)
    tamanho = len(arr)
    result = 0
    for idx, n in enumerate(arrSorted):
        aux = idx+1
        #Como o array está ordenado, somente precisa continuar calculando a diferença entre o item atual 'n' e os próximos elementos enquanto a aquela for menor ou igual a 'dif'
        while (aux < tamanho) and (abs(arrSorted[aux] - n) <= dif):
            if arrSorted[aux] - n == dif:
                result += 1
            aux += 1
    return(result)
  


if __name__ == '__main__':

    n = int(input("Digite a diferença buscada: "))
    arr = list(map(int, input("Digite os valores do array separados por espaço: ").rstrip().split()))
    
    rslt = diferenca(arr, n)
    print(f"Existe(m) {rslt} par(es) cuja diferença é {n}")
    
    
