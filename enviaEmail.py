import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mensagens import verif_se_email


# Enviar email com chave de confirmação para validar email
def enviar(email):
    chave_confirm = secrets.choice(range(10000, 99999))

    remetente_email = 'ricmcfer@gmail.com'
    senha = 'yuexqpvjovkfisud'

    destinatario_email = email
    assunto = 'Email de confirmação'
    mensagem = f'Deve introduzir o seguinte código para confirmar o seu email: {chave_confirm}'

    msg = MIMEMultipart()
    msg['From'] = remetente_email
    msg['To'] = destinatario_email
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente_email, senha)
        server.sendmail(remetente_email, destinatario_email, msg.as_string())
        return (chave_confirm, True)
    except:
        verif_se_email()
        return (chave_confirm, False)
