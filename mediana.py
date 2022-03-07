#Desafio de programação CAPGEMINI 02
#Questão 01
#Autor: Douglas Almeida Carneiro

from SortingAlgorithm import quickSort
from typing import Union


def mediana(arr: list) -> Union[int, float]:
    """Determina a mediana de um conjunto ímpar de valores numéricos

    :param arr: Array valores numéricos
    :return: Mediana
    """
    #Lança exceção caso a quantidade de elementos no arr não seja ímpar
    if (len(arr)>0) and (len(arr)%2 == 0):
        raise ValueError("Parâmetro 'arr' deve ter quantidade ímpar de elementos")
    
    #Lança exceção caso haja elementos não numéricos em arr
    for x in arr:
        if type(x) not in [int, float]:
            raise TypeError("Parâmetro 'arr' deve conter apenas valores numéricos") 

    #Lança exceção caso o array de entrada esteja vazio
    if len(arr) == 0:
        raise ValueError("Parâmetro 'arr' não pode ser vazio")

    #Ordena arr de forma crescente
    arrSorted = quickSort(arr)
    
    #A mediana será o elemento do meio no array ordenado
    meio = (len(arr) // 2)
    return arrSorted[meio]



if __name__ == '__main__':
    arr = list(map(int, input("Digite os valores do array separados por espaço: ").rstrip().split()))
    rslt = mediana(arr)
    print(f"A mediana de {arr} é {rslt}")
    
