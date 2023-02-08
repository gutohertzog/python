"""módulo para monitorar o arquivo binário"""
from classes import Cpf, Scanner


if __name__ == '__main__':
    arquivo: str = 'passador.txt'
    scan: Scanner = Scanner(arquivo)

    while True:
        cpf_input: str = scan.monitorador()

        # realiza uma validação preliminar antes de tornar objeto
        if Cpf.valida_input(cpf_input):
            cpf_cru: Cpf = Cpf.cria_cpf(cpf_input)

            # valida como objeto
            cpf_cru.valida_cpf()
            print(f'{cpf_cru = }')

            if cpf_cru.e_valido:
                scan.avisa_gui('True')
            else:
                print(f'{cpf_input = } - CPF inválido')
                scan.avisa_gui('False')
        else:
            print(f'{cpf_input = } - CPF inválido')
            scan.avisa_gui('False')
