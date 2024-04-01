import socket
import sys
import customtkinter as ctk
from crypto import value_decrypto
from mensagens import erroServidor
import json


host = 'localhost'
porta = 5555

# Conectar ao servidor
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, porta))
except Exception as erro:
    erroServidor(erro)
    sys.exit()


def enviar_dados(dados):
    client_socket.send(dados)


def receber_dados():
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            return message


def receber_mensagens(boxmensagens):
    while True:
        mensagem = receber_dados()
        if not mensagem:
            break
        msg = json.loads(mensagem)
        primeiro_dados = iter(msg.items())
        primeiro_item = next(primeiro_dados)
        if primeiro_item[0] == 'mensagem':
            boxmensagens.configure(state="normal")
            boxmensagens.insert(ctk.END, value_decrypto(msg['mensagem'][2:-1]))
            boxmensagens.configure(state="disabled")


def client_close():
    client_socket.close()
