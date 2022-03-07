#Função auxiliar para ordenação de arrays
#Autor: Douglas Almeida Carneiro

import math
import os
import random
import re
import sys


def quickSort(arr):
    """Ordena de forma crescente um array, utilizando o algoritmo QuickSort.

    :param arr: Array a ser ordenado
    :return: O array ordenado
    """
    #Se o array tem tamanho menor que 1, então ele já está ordenado
    if len(arr) <= 1:
        return arr
    #A chave é sempre primeiro item do array
    key = arr[0]
    #Obtem os elementos iguais à chave
    equal = [x for x in arr if x == key]
    #Obtem os elementos menores que a chave
    left = [x for x in arr if x < key]
    #Obtem os elementos maiores que a chave
    right = [x for x in arr if x > key]

    #Repete, recursivamente, o processo com os elementos maiores e menores que a chave
    leftSorted = quickSort(left)
    rightSorted = quickSort(right)
    
    #Mescla os arrays ordenados
    return  leftSorted + equal + rightSorted


