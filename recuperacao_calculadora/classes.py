"""módulo com as classes do projeto"""
from datetime import datetime


class Calculadora:
    """classe para realizar as operações de cálculo"""

    def __init__(self, conta: str) -> None:
        # conta recebida pelo usuário
        self.conta: str = conta.strip()
        # atributo para controlar o que salvar e onde salvar
        self.arq = Arquivo()

        # atributos para as operações
        self.num_1: int = 0
        self.num_2: int = 0
        self.oper: str = ''

    def realiza_conta(self) -> None:
        """método para realizar a conta própriamente dita"""
        if self.valida_entrada():
            separados: list[str] = self.conta.split()

            # converto direto para inteiro, pois já realizei a validação de
            # inteiro em valida_entrada
            self.num_1 = int(separados[0])
            self.oper = separados[1]
            self.num_2 = int(separados[2])

            # distribui a conta de acordo com o tipo de operação
            if self.oper == '+':
                self.soma()
            elif self.oper == '-':
                self.substracao()
            elif self.oper == '*':
                self.multiplicacao()
            elif self.oper == '/':
                self.divisao()
            else:
                self.potenciacao()

    def valida_entrada(self) -> bool:
        """método para validar a entrada dos valores"""
        # separo os números e os operadores em uma lista, que deverá ter 3
        # itens
        separados: list[str] = self.conta.split()

        # testa tamanho, qualquer coisa diferente de 3 é errado
        if len(separados) < 3:
            msg: str = 'digitou poucos termos'
            self.arq.salva_ruim(self.conta, msg)
            return False
        if len(separados) > 3:
            msg: str = 'digitou termos demais'
            self.arq.salva_ruim(self.conta, msg)
            return False

        # valida números
        try:
            # não pode receber float, por isso invalida números com ponto
            if '.' in separados[0]:
                raise ValueError
            separados[0] = int(separados[0])
        except ValueError:
            msg: str = 'o primeiro termo não é um número válido'
            self.arq.salva_ruim(self.conta, msg)
            return False
        try:
            # não pode receber float, por isso invalida números com ponto
            if '.' in separados[2]:
                raise ValueError
            separados[2] = int(separados[2])
        except ValueError:
            msg: str = 'o terceiro termo não é um número válido'
            self.arq.salva_ruim(self.conta, msg)
            return False

        # valida operador
        if not separados[1] in ['+', '-', '*', '/', '**']:
            msg: str = 'operador inválido'
            self.arq.salva_ruim(self.conta, msg)
            return False

        # se todos os testes deram ok, retorna para realizar a conta na
        # realiza_conta
        return True

    def soma(self) -> None:
        """módulo para realizar a soma dos valores"""
        result = self.num_1 + self.num_2
        self.arq.salva_bom(self.conta, result)

    def substracao(self) -> None:
        """módulo para realizar a subtração dos valores"""
        result = self.num_1 - self.num_2
        self.arq.salva_bom(self.conta, result)

    def multiplicacao(self) -> None:
        """módulo para realizar a multiplicação dos valores"""
        result = self.num_1 * self.num_2
        self.arq.salva_bom(self.conta, result)

    def divisao(self) -> None:
        """módulo para realizar a divisão dos valores"""
        try:
            if self.num_2 == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            msg: str = 'não é possível dividir por zero'
            self.arq.salva_ruim(self.conta, msg)
        else:
            result = self.num_1 / self.num_2
            self.arq.salva_bom(self.conta, result)

    def potenciacao(self) -> None:
        """módulo para realizar a potenciação dos valores"""
        result = self.num_1 ** self.num_2
        self.arq.salva_bom(self.conta, result)


class Arquivo:
    """classe para gerenciar os salvamentos em disco das operações"""

    def __init__(self, arq_bom: str = 'acertos.txt', arq_ruim: str = 'erros.log') -> None:
        self.arq_bom = arq_bom
        self.arq_ruim = arq_ruim

    def salva_bom(self, conta: str, total: int) -> None:
        """método para salvar no arquivo os bons cálculos"""
        msg: str = conta + ' = ' + str(total)

        # monta a data e hora atual
        agora: datetime = datetime.now()
        data_hora: str = f'{agora.day}/{agora.month}/{agora.year} '
        data_hora += f'{agora.hour}:{agora.minute}:{agora.second}.'
        data_hora += f'{agora.microsecond}'

        # monta o dicionário para salvar no arquivo
        bom: dict = {'operacao': conta}
        bom['resultado'] = total
        bom['data_hora'] = data_hora

        # mostra a mensagem e salva o resultado
        print(msg)
        with open(self.arq_bom, 'a', encoding='utf-8') as arq:
            arq.write(str(bom) + '\n')

    def salva_ruim(self, conta: str, msg: str) -> None:
        """método para salvar no arquivo os ruins cálculos"""
        # monta a data e hora atual
        agora: datetime = datetime.now()
        data_hora: str = f'{agora.day}/{agora.month}/{agora.year} '
        data_hora += f'{agora.hour}:{agora.minute}:{agora.second}.'
        data_hora += f'{agora.microsecond}'

        # monta o dicionário para salvar no arquivo
        ruim: dict = {'operacao': conta}
        ruim['resultado'] = msg
        ruim['data_hora'] = data_hora

        # mostra a mensagem e salva o resultado
        print(f'{conta} -> {msg}')
        with open(self.arq_ruim, 'a', encoding='utf-8') as arq:
            arq.write(str(ruim) + '\n')


if __name__ == '__main__':
    # casos de teste
    casos_teste = [
        '1 + 41', '47 + -5', '32 - -10', '45 - 3', '7 * 6', '42 / 1',
        '2 ** 10', '2 ** -5', '1+8', '2 -9', 'a + 8', 'meu nome aqui a',
        '19** 2', 'asdf - 5', '5--10', '58 - 10 + 5', '3.14 + 16', 'sair']

    for caso in casos_teste:
        if caso == 'sair':
            print('Encerrando')
            break
        calc = Calculadora(caso)
        calc.realiza_conta()
