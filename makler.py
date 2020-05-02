import requests

COINS = ['LTC','ETH','TRX','XRP']

tokok = "https://www.tokok.com/api/v1/depth?symbol={}_BTC"
bitbay = "https://bitbay.net/API/Public/{}BTC/orderbook.json"
biki = "https://openapi.biki.com/open/api/market_dept?symbol={}btc&type=step0"
latoken = "https://api.latoken.com/v2/marketOverview/orderbook/{}_BTC"


def getTokokMarket():
    print("Processing Tokok market")
    tokokMarket = {}
    for coin in COINS:
        coinInfo = {}
        print(coin)
        respons = requests.get(tokok.format(coin))
        coinInfo['asks'] = respons.json()['asks']
        coinInfo['bids'] = respons.json()['bids']
        tokokMarket[coin] = coinInfo
    return tokokMarket

def getBitbayMarket():
    print("Processing Bitbay market")
    bitbayMarket = {}
    for coin in COINS:
        coinInfo = {}
        print(coin)
        respons = requests.get(bitbay.format(coin))
        coinInfo['asks'] = respons.json()['asks']
        coinInfo['bids'] = respons.json()['bids']
        bitbayMarket[coin] = coinInfo
    return bitbayMarket

def getBikiMarket():
    print("Processing Biki market")
    bikiMarket = {}
    for coin in COINS:
        coinInfo = {}
        print(coin)
        respons = requests.get(biki.format(coin.lower()))
        coinInfo['asks'] = respons.json()['data']['tick']['asks']
        coinInfo['bids'] = respons.json()['data']['tick']['bids']
        bikiMarket[coin] = coinInfo
    return bikiMarket

def getLatokenMarket():
    print("Processing Latoken market")
    latokenMarket = {}
    for coin in COINS:
        coinInfo = {}
        print(coin)
        respons = requests.get(latoken.format(coin))
        coinInfo['asks'] = respons.json()['asks']
        coinInfo['bids'] = respons.json()['bids']
        latokenMarket[coin] = coinInfo
    return latokenMarket

def handle

marketsOrderbooks = {}
marketsOrderbooks['tokok'] = getTokokMarket()
marketsOrderbooks['bitbay'] = getBitbayMarket()
marketsOrderbooks['biki'] = getBikiMarket()
marketsOrderbooks['latoken'] = getLatokenMarket()


for marketName, orderbook in marketsOrderbooks.items():
    print(marketName)
    for crypto, orders in orderbook.items():
        print("Sprawdzam {} z {}".format(crypto, marketName))
        if(orders['asks']):
            bestAskOrder = orders['asks'][0]
            for otherMarketName, otherOrderbook in marketsOrderbooks.items():
                if(otherOrderbook[crypto]['bids']):
                    print("Kup za: {}, sprzedaj za {}".format(bestAskOrder,otherOrderbook[crypto]['bids'][0]))
                    if(float(bestAskOrder[0])<float(otherOrderbook[crypto]['bids'][0][0])):
                        print("WARTO!")


