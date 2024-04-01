from CTkMessagebox import CTkMessagebox

# -----------------Mensagens-------------------


def msg_login_encontrado(encontrado, nome):
    if encontrado == 'True':
        login = CTkMessagebox(title="Conta", message=f'Login efetuado com sucesso {nome}!!', icon="check", option_1="Continuar")
    else:
        login = CTkMessagebox(title="Erro", message='Não foi possível iniciar sessão.\nVerifique se o email e a password estão corretos.', icon="cancel")
    login.wait_window()


def erro_mail():
    erroMail = CTkMessagebox(title="Erro", message="Introduza um email válido", icon="cancel")
    erroMail.wait_window()


def erro_pass():
    erroPass = CTkMessagebox(title="Password Inválida", message="A password necessita de ter:\n1 - Uma Letra Maiuscula\n2 - Um número\n3 - Um caracter especial\n4 - No minimo 10 caracteres", icon="cancel")
    erroPass.wait_window()


def verif_se_email():
    veriEmail = CTkMessagebox(title="Erro", message='Erro ao enviar o email', icon="cancel")
    veriEmail.wait_window()


def chave_invalida():
    chaveInv = CTkMessagebox(title="Erro", message='Chave de confirmação inválida', icon="cancel")
    chaveInv.wait_window()


def sucesso():
    su = CTkMessagebox(title="Conta", message="Conta Criada com sucesso", icon="check", option_1="Continuar")
    su.wait_window()


def erroServidor(erro):
    erroServ = CTkMessagebox(title="Erro Servidor", message=f"Erro ao ligar ao Servidor:\n{erro}", icon="check", option_1="Continuar")
    erroServ.wait_window()
