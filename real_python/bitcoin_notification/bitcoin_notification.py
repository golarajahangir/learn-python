
import requests
import time
from datetime import datetime

BITCOIN_API_URL = "https://api.btcturk.com/api/v2/ticker?pairSymbol=BTCUSDT"
IFTTT_WEBHOOKS_URL="https://maker.ifttt.com/trigger/{}/with/key/mlIgTmJsJvG8cb0actBCFcZznfTDpa1FVzg9hLFQXW0"
BITCOIN_PRICE_THRESHOLD = 17000

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    return float(response_json['data'][0]['last'])


def post_ifttt_webhook(event, value):
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, json=data)

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    return '<br>'.join(rows)

def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        if len(bitcoin_history) == 5:
            post_ifttt_webhook('bitcoin_price_update', 
                               format_bitcoin_history(bitcoin_history))
            bitcoin_history = []
        time.sleep(2 * 60)
if __name__ == '__main__':
    main()
