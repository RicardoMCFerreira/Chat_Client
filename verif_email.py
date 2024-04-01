import re


# Verifica se o email introduzido é um email válido
def validar_email(email):
    # Expressão regular para validar o formato do email
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Verifica se o email corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False
