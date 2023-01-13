"""módulo de números de Fibonacci"""


def fib(n):
    """escreve a série de Fibonacci até n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    """retorna a série de Fibonacci até n"""
    resultado = []
    a, b = 0, 1
    while a < n:
        resultado.append(a)
        a, b = b, a+b
    return resultado


if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
