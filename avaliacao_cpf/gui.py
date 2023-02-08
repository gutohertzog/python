"""módulo do gui do programa"""
from tkinter import Button, END, Entry, Label, messagebox, Tk


def salva_e_verifica() -> None:
    """função para pegar o valor do campo ent_cpf que terá um CPF a ser
    validado"""
    arquivo: str = 'passador.txt'
    entrada: str = ent_cpf.get()

    if entrada != '':
        ent_cpf.delete(0, END)
        with open(arquivo, 'w', encoding='utf-8') as arq:
            arq.write(entrada)

        monitora_respota(entrada)


def monitora_respota(entrada):
    """fica lendo o arquivo de resposta para saber qual foi o resultado da
    validação"""
    while True:
        with open('resposta.txt', 'r', encoding='utf-8') as arq:
            conteudo: str = arq.read()
            conteudo = conteudo.strip()

            if not conteudo:
                continue

            # limpa o arquivo
            open('resposta.txt', 'w', encoding='utf-8').close()
            break

    mostra_resultado(entrada, conteudo)


def mostra_resultado(entrada, conteudo):
    """usa o mesagebox para mostrar a respota da validação ao usuário"""
    print(f'{entrada = }')
    print(f'{conteudo = }')
    if conteudo == 'True':
        messagebox.showinfo('Válido', 'CPF válido!')
    else:
        messagebox.showerror('Inválido', 'CPF inválido!')


def encerra() -> None:
    """função para encerrar a janela do GUI"""
    janela.destroy()


janela: Tk = Tk()
# definições da janela
janela.title('Validador CPF')
janela.iconbitmap('git.ico')
janela.minsize(width=400, height=300)
janela.maxsize(width=600, height=400)

# label do título do programa
lbl_titulo: Label = Label(
    janela, text='VALIDADOR DE CPF', font=('Arial', 20))
lbl_titulo.pack()

# label pedindo o CPF
lbl_txt_cpf: Label = Label(janela, text='Seu CPF : ')
lbl_txt_cpf.pack()

# campo onde o CPF será digitado
ent_cpf: Entry = Entry(janela)
ent_cpf.pack()

# criando um botão de submit
btn_cpf: Button = Button(janela, text="Enviar", command=salva_e_verifica)
btn_cpf.pack()

# botão para encerrar o programa
btn_encerra = Button(janela, text="Encerrar", command=encerra)
btn_encerra.pack()

janela.mainloop()
