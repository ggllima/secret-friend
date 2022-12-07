# configs email
import smtplib
from data_account import infos

print(infos['login'])

# S M T P - Simples Mail transfer protocol
# Para criar o servidor e enviar o e-mail
# Conectar servidor SMTP

host = "smtp.gmail.com"
port = "587"
login = infos['login']
password = infos['password']

def connection_email(host, port, login, password):
    server = smtplib.SMTP(host, port)

    server.ehlo()
    server.starttls()

    try:
        server.login(login, password)
        print("Login success")
    except smtplib.SMTPAuthenticationError as error:
        print("Authentication failed. Check credentials in config folder: ",error)
    except TypeError:
        print("Authentication failed (type error). Check credentials in config folder")
        
    return server

