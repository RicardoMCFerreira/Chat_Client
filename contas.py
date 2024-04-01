import json
from crypto import *
from conectServidor import *
from mensagens import msg_login_encontrado

# Criar nova conta


def nova_conta(novom, novap, nome_util):
    dados_enviar = {'novo_mail': str(value_encrypto(novom)), 'nova_pass': str(value_encrypto(novap)), 'nome_utilizador': nome_util}
    # Enviar o dicionário para o servidor
    dados = json.dumps(dados_enviar).encode('utf-8')
    enviar_dados(dados)


# Verificar se utilizador existe
def iniciar_sessao(email, password):

    # Enviar o dicionário para o servidor
    dados_enviar = {'email': str(value_encrypto(email)), 'password': str(value_encrypto(password))}
    dados = json.dumps(dados_enviar).encode('utf-8')
    enviar_dados(dados)
# Resposta do servidor
    dados_recebidos = json.loads(receber_dados())
    encontrado = dados_recebidos['encontrado']
    nome = dados_recebidos['nome']
    if encontrado in ('True', 'False'):
        msg_login_encontrado(encontrado, nome)
        return (encontrado, nome)


def remover_conta():
    dados_enviar = {'remover': 'True'}
    dados = json.dumps(dados_enviar).encode('utf-8')
    enviar_dados(dados)
