def executar(funcao):
    if callable(funcao):  # Dessa forma se ele não puder ser chamado o python vai simplesmente ignorá-lo
        funcao()  # parenteses está invocando uma função


def bom_dia():
    print('Bom dia')


def boa_tarde():
    print('Boa tarde')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    # executar (1) vai gerar um problema pois o objeto int não é possivel ser chamado
