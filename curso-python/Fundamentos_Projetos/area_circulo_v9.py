#!/usr/local/bin/python3
import math


def circulo(raio):
    return math.pi * float(raio) ** 2
# Def define a função
# Função é um algoritmo com nome basicamente


if __name__ == '__main__':
    raio = input('Informe o raio:')
    area = circulo(raio)
    print('Área do círculo =', area)


# Para duplicar ALT + SHIFT + setinha pra baixo
# print (1 + 2) apertando CTRL + ALT + N e selecionando alguma linha em específico ele só vai executar apenas a que você especificou
# Lembre-se de usar cd para ir na pasta que deseja e CHAMAR O INTERPRETADOR DO PYTHON(python.exe)
# Pode se colocar um apelido em um arquivo com import area_circulo_v9 as v9 que fica mais facil e torna o código mais simples e interessante.