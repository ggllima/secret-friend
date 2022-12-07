from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
#from config_email import login, server

host = "smtp.gmail.com"
port = "587"
login = "guilhermelima.rp@gmail.com"
password = "thxzwhalbpvnccpu"

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


def send_email(login:str, recipient:list, subject:str, message:str):
    
    email_message = MIMEMultipart()
    email_message['From'] = login
    email_message['To'] = ','.join(recipient)
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message, 'html'))
    
    server.sendmail(email_message['From'], email_message['To'], email_message.as_string())
    
    server.quit()

message = """
Olá !
<br>
<br>
Identificamos documentos gerados recentemente na plataforma da Looplex que não foram finalizados. Criamos um relatório (documento em anexo) para que possa analisá-los e tomar as providências necessárias, seja para removê-los, seja completá-los.
<br>
<br>
Ficamos à disposição para quaisquer esclarecimentos.
<br>
<br>
Atenciosamente,
<br>
<br>

<img alt="Footer" height="auto" src="https://cdn-icons-png.flaticon.com/512/6259/6259639.png" style="border:none;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="175" />
"""


send_email(login, ["ggllima@usp.br"], "teste pro amigo secreto", message)