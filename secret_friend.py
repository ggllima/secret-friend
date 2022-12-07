from generate_email import send_email
from config_email import connection_email, host, port, login, password
from messages.messages import messages
import random

emails = {'Esther':'estherlira12@yahoo.com',
          'Guilherme':'ggllima@usp.br',
          'Bianca':'biancagoferrao@gmail.com',
          'Roberta':'roberta.moraes@estudante.ufscar.br',
          'Kenzo':'kenzomelowaki@gmail.com',
          'Luis':'timoteootavioluis@gmail.com',
          'Julia':'juliamontedioca@gmail.com',
          'Vinicius':'viniimato@gmail.com',
          'Rachel':'domenerachel1@gmail.com'}

lista_fixa_amigos = {'Julia':5,'Bianca':6,'Esther':7,'Roberta':1, 'Vinicius':1,'Rachel':2,'Kenzo':3,'Guilherme':4, 'Luis':9}
lista_de_sorteio = ['Roberta','Luis','Rachel','Kenzo','Guilherme','Julia','Bianca','Vinicius','Esther']

dict_sorteio = {}

for amigo in lista_fixa_amigos:
    flag_repeat = False
    
    while flag_repeat == False:
        amigo_secreto = random.choice(lista_de_sorteio)
        if lista_fixa_amigos[amigo] != lista_fixa_amigos[amigo_secreto]:
            flag_repeat = True
        else:
            flag_repeat = False
            
        
    lista_de_sorteio.remove(amigo_secreto)
    dict_sorteio.update({amigo:amigo_secreto})

for person in emails:
    server = connection_email(host, port, login, password)
    final_message = messages[person].format(dict_sorteio[person])
    send_email(server, login, [emails[person]], "CONVITE PARA AMIGO SECRETO TUDO EM CAPS LOCK FODA-SE",final_message)

