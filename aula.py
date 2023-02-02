"""docstring"""

if __name__ == '__main__':
    numero_1 = 4
    numero_2 = 5

    print(numero_1 * numero_2)
    resultado = numero_1 + numero_1 + numero_1 + numero_1 + numero_1
    print(resultado)

    resultado = 0
    for _ in range(numero_2):
        resultado = resultado + numero_1
    print(resultado)

    contador = numero_2
    resultado = 0
    while contador > 0:
        resultado = resultado + numero_1
        contador -= 1
    print(resultado)

    # 4 x 5
    def multiplicacao_bracal(valor: int, cont: int) -> int:
        """sou o docstring"""
        if cont == 1:
            return valor
        return valor + multiplicacao_bracal(valor, cont-1)

    print(multiplicacao_bracal(numero_1, numero_2))

    nome: str = 'aragorn'

    def divide_nome(texto: str) -> list[str]:
        """retorna uma string dividida"""
        return texto.split()

    print(divide_nome(nome))


class Teste:
    def __init__(self, valor) -> None:
        self.valor = valor

    def mostra_valor(self, algo):
        print(algo)
        print(self.valor)


meu_objeto = Teste(5)
# objeto.mostra_valor(10)

Teste.mostra_valor(meu_objeto, 10)
