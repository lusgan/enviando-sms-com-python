# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 23:13:14 2023

@author: balbi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:40:36 2023

@author: balbi
"""

from twilio.rest import Client

account_sid = "SUA SID fornecida pela twilio"
auth_token = "SEU TOKEN FORNECIDO PELA TWILIO"

#esse é o meu telefone, ao criar uma conta na twilio voce tera o seu
remetente = "+16206340557"
destinatario = "NUMERO DO DESTINATARIO"

client = Client(account_sid,auth_token)

message = client.messages.create(to = destinatario, from_ = remetente, body = "ola, esse é um exemplo de mensagem")
print(message.sid)