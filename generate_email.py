from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(server, login:str, recipient:list, subject:str, message:str):
    
    email_message = MIMEMultipart()
    email_message['From'] = login
    email_message['To'] = ','.join(recipient)
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message, 'html'))
    
    server.sendmail(email_message['From'], email_message['To'], email_message.as_string())
    
    server.quit()