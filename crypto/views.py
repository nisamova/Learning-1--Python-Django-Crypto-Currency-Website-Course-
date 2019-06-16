from django.shortcuts import render

# Added this to give instruction to urls.py-crypto file to request/render hoempage
def home(request):
    import requests
    import json
    #Api and Pyton/Django code for currency ticker NSI
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XML,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    #Api and Pyhton/Django code for Cryto News NSI
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price':price}) # python dictionary example NSI.
