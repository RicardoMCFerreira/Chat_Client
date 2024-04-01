import customtkinter as ctk
from contas import *
from janelaNovaConta import janelaNovaConta
from janelaChat import janelaChat

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


class Login:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.geometry("520x225+500+300")
        self.janela.title("Login")

        container_cima = ctk.CTkFrame(self.janela)
        container_cima.grid(row=0, column=0, padx=10, pady=20)
        container_cima.configure(fg_color='transparent')

        container_baixo = ctk.CTkFrame(self.janela)
        container_baixo.grid(row=1, column=0, padx=10, pady=0)
        container_baixo.configure(fg_color='transparent')

        email = ctk.CTkEntry(container_cima, placeholder_text='Email', width=400)
        email.grid(row=0, column=0, padx=50, pady=10)

        password = ctk.CTkEntry(container_cima, placeholder_text='Password', show='*', width=400)
        password.grid(row=1, column=0, padx=50, pady=10)

        botaoLogin = ctk.CTkButton(container_baixo, text="Login", command=lambda: novoLogin(email.get(), password.get(), self.janela))
        botaoLogin.grid(row=0, column=1, padx=10, pady=0)

        botaoNovaConta = ctk.CTkButton(container_baixo, text='Nova Conta', command=lambda: janelaNovaConta(self.janela))
        botaoNovaConta.grid(row=0, column=2, padx=10, pady=0)

        botaoSair = ctk.CTkButton(container_baixo, text='Sair', command=lambda: sair(self.janela))
        botaoSair.grid(row=0, column=3, padx=10, pady=10)

        self.janela.mainloop()


def novoLogin(email, password, janela):
    sucesso, nome = iniciar_sessao(email, password)
    if sucesso == 'True':
        janela.withdraw()
        janelaChat(nome)


def sair(janela):
    remover_conta()
    janela.quit()
