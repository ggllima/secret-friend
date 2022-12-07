from generate_email import send_email
from config_email import connection_email, host, port, login, password
from messages.messages import messages

for message in messages:
    server = connection_email(host, port, login, password)
    send_email(server, login, ["ggllima@usp.br"], "teste com as mensagens corrigidas",messages[message])