import requests 
from api import url, cryptcur_api
from time import sleep

def get_last_update(offset):
    params = {'timeout': 100, 'offset': offset}
    parsed_data = requests.get(url+'getUpdates', data = params)
    response = parsed_data.json()
    return response['result']
  
def send_mes(chat_id, message_text):
    block = {'chat_id' : chat_id, 'text' : message_text}
    response = requests.post(url+'sendMessage', data = block)

def get_btc_price(cryptcur_api):
    parsed_data = requests.get(cryptcur_api + 'btc' + '-usd/')
    response = parsed_data.json()
    return response['ticker']['price']

def get_eth_price(cryptcur_api):
    parsed_data = requests.get(cryptcur_api + 'eth' + '-usd/')
    response = parsed_data.json()
    return response['ticker']['price']

def main():
    offset = 0
    while True:
        updates_list = get_last_update(offset)
        for update in updates_list:
            chat_id = update['message']['chat']['id']
            first_name = update['message']['from']['first_name']
            message_text = update['message']['text']
            if message_text == '/btc':
                send_mes(chat_id, 'Current BTC price is: ' +str(get_btc_price(cryptcur_api)) + 'USD' )
            elif message_text == '/eth':
                send_mes(chat_id, 'Current ETH price is: ' +str(get_eth_price(cryptcur_api)) + 'USD' )
            elif message_text == '/start':
                send_mes(chat_id, 'Hey, {}! This Bot shows you current prices of Bitcoin and Ethereum. Please, type /help'.format(first_name))
            elif message_text == '/help':
                send_mes(chat_id, 'For getting exchange rates, please, press /btc or /eth correspondingly'.format(first_name))
            else:
                send_mes(chat_id, 'Incorrect command. Press "/start" for help')
            print(message_text + ' user: ' + first_name)
            offset = updates_list[-1]['update_id'] + 1
        sleep(1)
if __name__ == '__main__':
    main()
