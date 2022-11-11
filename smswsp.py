from twilio.rest import Client
import time
import requests
import os

account_sid = 'AC5487bfc745758cd20933162232813171'

auth_token = "3f3d93db6cfd977e7a994fafbd4e9d5b"

client = Client(account_sid, auth_token)


urlll = 'https://libre-api-4bfd9-default-rtdb.firebaseio.com/api/llamadass.json'

ax = requests.get(urlll)
jsooon = ax.json()
timeee = jsooon['timee']
while 1<2:
    print('Inició')
    time.sleep(timeee)
    message = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body='Holi',      
        to='whatsapp:+51951400060') 
    print(message.sid)
