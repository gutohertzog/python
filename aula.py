"""teste de recursão"""
from random import randint


def multiplicacao(valor, i) -> int:
    if i == 0:
        return 0
    return valor + multiplicacao(valor, i-1)


if __name__ == '__main__':
    print(multiplicacao(10, 2))


class No:
    def __init__(self, valor: int, esquerda: int = None, direita: int = None) -> None:
        self.valor: int = valor
        self.esquerda: int = esquerda
        self.direita: int = direita


def insere(no: No, valor: int) -> No:
    if no is None:
        return No(valor)
    if valor < no.valor:
        no.esquerda = insere(no.esquerda, valor)
    else:
        no.direita = insere(no.direita, valor)
    return no


def buscador(no: No, alvo: int) -> bool:
    if no is None:
        return False

    if no.valor == alvo:
        return True

    return buscador(no.esquerda, alvo) or buscador(no.direita, alvo)


def cria_arvore_ordenada(lista: list[int]) -> No:
    raiz = None
    for valor in lista:
        raiz: No = insere(raiz, valor)
    return raiz


def mostra_arvore(no: No, direcao: int = 0):
    if no is None:
        return
    if direcao == 0:
        print(no.valor)
        mostra_arvore(no.esquerda, -1)
        mostra_arvore(no.direita, 1)
    elif direcao == -1:
        print(" " * 4 * abs(direcao) + str(no.valor))
        mostra_arvore(no.esquerda, direcao - 1)
        mostra_arvore(no.direita, direcao + 1)
    else:
        print(" " * 4 * abs(direcao) + str(no.valor))
        mostra_arvore(no.esquerda, direcao - 1)
        mostra_arvore(no.direita, direcao + 1)


def mostra_arvore_a(node: No, level: int = 0):
    if node is None:
        return
    print(" " * 4 * (level + 1) + str(node.valor))
    mostra_arvore_a(node.esquerda, level + 1)
    mostra_arvore_a(node.direita, level + 1)


valores: list[int] = [randint(1, 100) for _ in range(100)]

arvore: No = cria_arvore_ordenada(valores)
print(buscador(arvore, 100))
print(buscador(arvore, 8))
mostra_arvore(arvore)
