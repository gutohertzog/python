"""módulo com as classes do programa"""
from datetime import datetime
from time import sleep
import constantes as const


class Cpf:
    """classe para gereciar o CPF"""

    def __init__(self, cpf: str) -> None:
        # cpf recebido
        self.cpf_rec: str = cpf
        # cpf apenas números
        self.cpf_num: str = ''.join(c for c in cpf if c.isdigit())
        # self.cpf_num: str = ''.join(filter(str.isdigit, cpf))
        # self.cpf_num: str = cpf.replace('.', '').replace('-', '')
        # cpf formatado
        self.cpf_form: str = self.cpf_num[:3] + '.' + self.cpf_num[3:6] + \
            '.' + self.cpf_num[6:9] + '-' + self.cpf_num[9:]
        self.arquivo: Arquivo = Arquivo()
        # atributo para controlar se o CPF é válido
        # será True quando a validação for bem sucedida
        self.e_valido: bool = False

    def calcula_soma(self, mult: int) -> int:
        """realiza o cálculo da soma dos dígitos"""
        return sum(int(d) * (mult - i) for i, d in enumerate(self.cpf_num[:mult-1]))

    def calcula_digito(self, soma: int) -> int:
        """calcula o dígito verificador"""
        return 0 if (soma % 11) < 2 else 11 - (soma % 11)

    def valida_cpf(self) -> None:
        """método que vai validar efetivamente o CPF"""
        for i in range(10, 12):
            digito: int = self.calcula_digito(self.calcula_soma(i))
            if digito != int(self.cpf_num[i-12]):
                i -= 9  # subtrai para salvar o valor do dígito
                msg: str = f'{i}º dígito inválido'
                Arquivo.salva_erro(self.cpf_form, msg)
                print(msg)
                return

        print('CPF válido')
        self.e_valido = True
        self.arquivo.salva_valido(self.cpf_rec)
        return

    @staticmethod
    def valida_input(cpf: str) -> bool:
        """realiza os testes mínimo de validação da digitação do CPF"""
        try:
            # remove espaços em branco antes e depois
            # objetos do tipo int não tem o método strip(), por isso o try
            cpf: str = cpf.strip()
        except AttributeError:
            msg: str = 'de alguma forma, foi enviado um número!'
            Arquivo.salva_erro(str(cpf), msg)
            return False

        # testa se foi enviado apenas ponto e números
        count: dict[str, int] = {
            'traco': 0,
            'ponto': 0,
            'numero': 0,
        }
        for letra in cpf:
            if letra == '-':
                count['traco'] += 1
            elif letra == '.':
                count['ponto'] += 1
            elif letra.isdigit():
                count['numero'] += 1
            else:
                msg: str = 'caracter inválido digitado'
                Arquivo.salva_erro(cpf, msg)
                return False

        # mesmo vindo apenas números, pontos e traços, ainda podem vir cpf
        # com 14 núemros, 10 traços, 5 pontos, etc
        if count['traco'] > 1 or count['ponto'] > 2 or count['numero'] > 11:
            msg: str = 'quantidade de traços, ponto ou números inválida'
            Arquivo.salva_erro(cpf, msg)
            return False

        return True

    @classmethod
    def cria_cpf(cls, cpf_novo: str) -> 'Cpf':
        """retorna um objeto da classe CPF após validar o input"""
        # print(type(cpf_novo))
        return cls(cpf_novo)

    def __str__(self) -> str:
        """mostra apenas o CPF formatado"""
        return self.cpf_form

    def __repr__(self) -> str:
        """mostra a classe e o cpf recebido"""
        return f'Cpf({self.cpf_rec})'


class Arquivo:
    """classe para realizar as gerências de arquivos"""
    __arq_erro: str = const.ARQ_ERRO
    __arq_valido: str = const.ARQ_VALIDOS

    def __init__(self) -> None:
        pass

    def salva_valido(self, cpf: str) -> None:
        """salva o CPF válido"""
        agora: datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(self.__arq_valido, 'a', encoding=const.ENCODING) as arq:
            para_salvar: str = cpf + ' - (' + agora + ')\n'
            arq.write(para_salvar)

    @staticmethod
    def limpa_arquivos() -> None:
        """métodos para limpar os arquivos, usado para DEV"""
        open(Arquivo.__arq_erro, 'w', encoding=const.ENCODING).write()
        open(Arquivo.__arq_valido, 'w', encoding=const.ENCODING).write()

    @staticmethod
    def salva_erro(cpf: str, msg: str) -> None:
        """salva o CPF inserido errado em qualquer etapa"""
        agora: datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(Arquivo.__arq_erro, 'a', encoding=const.ENCODING) as arq:
            para_salvar: str = cpf + ' - (' + agora + ') : ' + msg + '\n'
            arq.write(para_salvar)


class Scanner:
    """classe responsável por monitorar o arquivo que será preenchido pela
    GUI com o CPF."""

    def __init__(self, nome_arq: str) -> None:
        self.nome_arquivo: str = nome_arq
        self.delta_t: int = 1

    def monitorador(self) -> str:
        """monitora o arquivo a cada segundo"""
        while True:
            with open(self.nome_arquivo, "r", encoding=const.ENCODING) as arq:
                valor: str = arq.read()
                valor: str = valor.strip()
                if valor:
                    open(self.nome_arquivo, 'w', encoding=const.ENCODING).close()
                    return valor
                sleep(self.delta_t)

    def avisa_gui(self, resultado: str) -> None:
        """método para salvar True ou False em um arquivo de texto, que será
        lido pelo GUI para então mostrar se o CPF é válido ou não"""
        with open('resposta.txt', 'w', encoding=const.ENCODING) as arq:
            arq.write(resultado)

    def __str__(self) -> str:
        return 'classe Scanner'


if __name__ == '__main__':
    casos: list[str] = ['111.444.777-315', '11111111111', 111222444555,
                        '111.444.777-15', '.........--', '12345678-98..',
                        '111.444.777-36', '111.444.777-35', '111.444.77735',
                        '111.444777-35', '111444.77735']

    for caso in casos:
        if Cpf.valida_input(caso):
            cpf_cru: Cpf = Cpf.cria_cpf(caso)
            cpf_cru.valida_cpf()
            print(cpf_cru)
        else:
            print('CPF inválido')
