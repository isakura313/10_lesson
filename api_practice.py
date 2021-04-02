import json
import requests
import time

CODE = input('ВВедите код валют. Курс можно посмотреть здесь https://www.coindesk.com/coindesk-api').strip().upper()
adr = f'https://api.coindesk.com/v1/bpi/currentprice/{CODE}.json'

while True:
    info = requests.get(adr)
    data = info.text
    data = json.loads(data)

    print("Дата обновления Курса по BTC", data['time']['updated'])
    print(f' Курс {data["bpi"]["USD"]["code"]}', data['bpi']['USD']['rate'])
    print(f' Курс {data["bpi"][CODE]["code"]}', data['bpi'][CODE]['rate'])
    time.sleep(3)
