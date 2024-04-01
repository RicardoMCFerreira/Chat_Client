import re
import secrets


# Verifica se a password introduzida tem as caracteristicasnecessárias
def verifica_password(password):
    # para verificar se há caracteres especiais
    padrao_especiais = re.compile(r'[^a-zA-Z0-9\s]')
    # para verificar se há números
    padrao_numeros = re.compile(r'\d')
    # para verificar se há pelo menos uma letra maiúscula
    padrao_maiuscula = re.compile(r'[A-Z]')

    if padrao_especiais.search(password) and padrao_numeros.search(password) and padrao_maiuscula.search(password) and len(password) >= 10:
        return True
    else:
        return False


# Cria uma password automática
def nova_pass_auto():
    while True:
        nova_pass = secrets.token_urlsafe(7)
        if verifica_password(nova_pass) == True:
            break
    return nova_pass
