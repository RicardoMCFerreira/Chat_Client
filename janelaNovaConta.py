import customtkinter as ctk
from contas import *
from verif_pass import *
from verif_email import validar_email
from enviaEmail import enviar
from mensagens import *

auto = False


def janelaNovaConta(janela):
    janela.withdraw()
    janelaNovo = ctk.CTk()
    janelaNovo.geometry("520x275+500+300")
    janelaNovo.title("Novo Utilizador")

    container_cima = ctk.CTkFrame(janelaNovo)
    container_cima.grid(row=0, column=0, padx=10, pady=20)
    container_cima.configure(fg_color='transparent')

    container_baixo = ctk.CTkFrame(janelaNovo)
    container_baixo.grid(row=1, column=0, padx=10, pady=0)
    container_baixo.configure(fg_color='transparent')

    novomail = ctk.CTkEntry(container_cima, placeholder_text='Email')
    novomail.configure(width=400)
    novomail.grid(row=0, column=0, padx=50, pady=10)

    novapassword = ctk.CTkEntry(container_cima, placeholder_text='Password')
    novapassword.configure(width=400)
    novapassword.grid(row=1, column=0, padx=50, pady=10)

    nomeUtilizador = ctk.CTkEntry(container_cima, placeholder_text='Nome Utilizador')
    nomeUtilizador.configure(width=400)
    nomeUtilizador.grid(row=2, column=0, padx=50, pady=10)

    checkbox = ctk.CTkCheckBox(container_cima, text='Pass Auto', command=lambda: passAuto(novapassword, checkbox.get()))
    checkbox.grid(row=3, column=0, padx=10, pady=0)

    botaoLogin = ctk.CTkButton(container_baixo, text="Criar Conta", command=lambda: criarConta(novomail.get(), novapassword.get(), nomeUtilizador.get(), janela, janelaNovo))
    botaoLogin.grid(row=0, column=1, padx=10, pady=0)

    botaoSair = ctk.CTkButton(container_baixo, text='Voltar', command=lambda: voltar(janela, janelaNovo))
    botaoSair.grid(row=0, column=3, padx=10, pady=10)

    janelaNovo.mainloop()


def criarConta(novomail, novapassword, nomeUtilizador, janela, janelaNovo):
    if novomail != '' and novapassword != '':
        if validar_email(novomail) == True:
            if verifica_password(novapassword) == True:
                chave_confirma, enviou = enviar(novomail)
                if enviou == True:
                    confirmar(chave_confirma, novomail,
                              novapassword, nomeUtilizador, janela, janelaNovo)
            else:
                erro_pass()
        else:
            erro_mail()


def confirmar(chave_confirma, novo_mail, nova_pass, nomeUtilizador, janela, janelaNovo):
    cod = ctk.CTkInputDialog(
        text="Introduza a chave de verificação:", title="Confirmar")
    codigo = cod.get_input()
    if codigo != '':
        if str(chave_confirma) == codigo:
            nova_conta(novo_mail, nova_pass, nomeUtilizador)
            sucesso()
            voltar(janela, janelaNovo)
        else:
            chave_invalida()


def passAuto(novapassword, auto):
    tamanho = len(novapassword.get())
    if auto == 1:
        novapassword.delete(0, tamanho)
        novapassword.insert(0, nova_pass_auto())
    else:
        novapassword.delete(0, tamanho)


def voltar(janela, janelaNovo):
    janelaNovo.destroy()
    janela.deiconify()
