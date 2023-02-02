"""pass"""
import time

while True:
    time.sleep(1)
    with open('monitorado.txt', 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
        if conteudo:
            open('monitorado.txt', 'w', encoding='utf-8').close()
            print(f'{conteudo.strip() = }')
        else:
            print('não tem nada no arquivo')
