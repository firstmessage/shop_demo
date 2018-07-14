#bot600954501:AAE9GxvpjuY-xEaNndVlapf6_UzgdKKMEWU

import requests
from time import sleep

#входные переменные 
token="bot600954501:AAE9GxvpjuY-xEaNndVlapf6_UzgdKKMEWU"


# получения апдейта от телеграмма
def get_bot_updates(limit, offset):
    url = "https://api.telegram.org/"+token+"/getUpdates" 
	
    
    par = {'limit': limit, 'offset': offset} 

    try:
        result = requests.get(url, params=par) # запрос
    except:
        print('get update error')
        return False 

    if (not result.status_code == 200): # проверим статус пришедшего ответа
        return False
    
	
    decoded = result.json()
    
    #print(decoded)

    if ('result' in decoded):
        if (len(decoded['result'])>0):
            return decoded ['result']
    
    return 0

# отправка собщения по id чата и сообщения на входе функции 
def send_bot_sessage(chat_id, text):
    url = "https://api.telegram.org/"+token+"/sendMessage" 
	
    
    par = {'chat_id': chat_id, 'text': text} 

    try:
        result = requests.get(url, params=par)
    except:
        print('send message error')
        return False
    
    if (not result.status_code == 200): # проверим статус пришедшего ответа
        return False

    #print (result.json())
    decoded = result.json()
    return decoded

#https://api.cryptonator.com/api/ticker/btc-usd курс биткоина 
#https://api.cryptonator.com/api/ticker/eth-usd курс эфириума

def get_bot_exchenge(doll):
    url = "https://api.cryptonator.com/api/ticker/"+doll+"-usd" 
	
    try:
        result = requests.get(url)
    except:
        print('get EX error')
        return False
        

    #print (result.status_code)
    if not result.status_code == 200: # проверим статус пришедшего ответа
        return False
    
    try:
        decode=result.json()
        if (decode['success']==True) : 
            return decode['ticker']['price']
        else :
            return 'ошибка запроса, попробуйте еще раз позже'

    except:
        print('get EX error')
        return 'ошибка запроса, попробуйте еще раз позже'

    
     
    

#print(result) 
  
# Получим только пять апдейтов
# словарь message > 
# from отправитель  'is_bot': False не бот  
# 'chat': {'id': 520399338 'type': 'private'} 
# 'text': 'Хе хе'

new_offset=0
update_id=0
text=''

while True:
    
    try:
        result=get_bot_updates(5, new_offset)  

        if (result != 0 or result!=False):

            for item in result:
                text = item['message']['text'] #сообщение
                chat_id = item['message']['chat']['id'] #id чата отправителя
                update_id = item['update_id']

                if (text=='/start'):
                    send_bot_sessage(chat_id, 'Бот \nВыводит актуальный курс биткоина  /btc \nВыводит актуальный курс эфириума /eth')
                elif (text=='/btc'):
                    send_bot_sessage(chat_id, 'Актуальный курс биткоина USD = '+get_bot_exchenge('btc'))
                elif (text=='/eth'):
                    send_bot_sessage(chat_id, 'Актуальный курс эфириума USD = '+get_bot_exchenge('eth'))
                else:
                    send_bot_sessage(chat_id, 'команда не распознана \n Бот \nВыводит актуальный курс биткоина  /btc \nВыводит актуальный курс эфириума /eth')
        new_offset = update_id + 1

    except KeyboardInterrupt: # порождается, если бота остановил пользователь
        print('Interrupted by the user')
        break
    
    sleep(0.5)


    
    

 