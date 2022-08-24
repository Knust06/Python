#!/usr/local/bin/python3
import math


def circulo(raio):
    print('Área do círculo =', math.pi * float(raio) ** 2)
# Def define a função


if __name__ == '__main__':
    raio = input('Informe o raio:')
    circulo(raio)


# Para duplicar ALT + SHIFT + setinha pra baixo
# print (1 + 2) apertando CTRL + ALT + N e selecionando alguma linha em específico ele só vai executar apenas a que você especificou
# Lembre-se de usar cd para ir na pasta que deseja e CHAMAR O INTERPRETADOR DO PYTHON(python.exe)
