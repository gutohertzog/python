"""busca por palavras no arquivo"""

if __name__ == '__main__':
    with open('..\\lord-of-the-rings.txt', 'r', encoding='utf-8') as arq:
        texto: str = arq.read()

    nomes: list[str] = ['Gandalf', 'Frodo', 'Sauron', 'Sam', 'Saruman']
    for nome in nomes:
        contagem: int = texto.count(nome)
        print(f'A contagem de {nome} é {contagem}.')
