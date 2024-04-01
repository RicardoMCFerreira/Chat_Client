import sys
import threading
import customtkinter as ctk
import json
from contas import remover_conta
from conectServidor import enviar_dados, receber_mensagens
from crypto import value_encrypto


def fechar():
    remover_conta()
    sys.exit()


def enviarNova(boxmensagens, novamensagem, nome):
    mensagem = str(f'{nome} - {novamensagem.get()}\n')
    dados_enviar = {'mensagem': str(value_encrypto(mensagem))}
    dados = json.dumps(dados_enviar).encode('utf-8')
    enviar_dados(dados)
    boxmensagens.configure(state="normal")
    boxmensagens.insert(ctk.END, f'Eu: {novamensagem.get()}\n')
    novamensagem.delete(0, len(novamensagem.get()))
    boxmensagens.configure(state="disabled")


def janelaChat(nome):
    janelaMensagens = ctk.CTk()
    janelaMensagens.geometry("840x700+500+50")
    janelaMensagens.title("Chat")

    container_cima = ctk.CTkFrame(janelaMensagens)
    container_cima.grid(row=0, column=0, padx=10, pady=20)
    container_cima.configure(fg_color='transparent')

    container_baixo = ctk.CTkFrame(janelaMensagens)
    container_baixo.grid(row=1, column=0, padx=10, pady=0)
    container_baixo.configure(fg_color='transparent')

    boxmensagens = ctk.CTkTextbox(container_cima, width=800, height=500, state="disabled")
    boxmensagens.grid(row=0, column=0, padx=10, pady=10)

    novamensagem = ctk.CTkEntry(container_baixo, placeholder_text='Mensagem', width=750)
    novamensagem.grid(row=0, column=0, padx=0, pady=10)

    enviar = ctk.CTkButton(container_baixo, text='Enviar', command=lambda: enviarNova(boxmensagens, novamensagem, nome), width=10)
    enviar.grid(row=0, column=1, padx=2, pady=10)

    sair = ctk.CTkButton(container_baixo, text='Sair', command=fechar)
    sair.grid(row=1, column=0, padx=10, pady=30)

    threading.Thread(target=receber_mensagens, args=(boxmensagens,), daemon=True).start()

    janelaMensagens.mainloop()
