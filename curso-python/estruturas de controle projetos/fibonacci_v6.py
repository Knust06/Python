# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(quantidade - 2): # Ou range(2, quantidade)
        resultado.append(sum(resultado[-2:])) #-2: ele pega sempre os dois ultimos elementos dando o resultado do desafio
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    #Listar os 20 primeiros números da sequência
    for fib in fibonacci(30):
        print(fib)
