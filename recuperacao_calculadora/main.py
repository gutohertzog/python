"""módulo principal que será chamado"""
from classes import Calculadora


if __name__ == '__main__':
    while True:
        try:
            entrada = input('Digite uma conta : ')
        except KeyboardInterrupt:
            print('digite "sair" para sair do programa!')
        else:
            if entrada == 'sair':
                print('Encerrando')
                break
            calc = Calculadora(entrada)
            calc.realiza_conta()
