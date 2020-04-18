import requests
import time

#coins = ['btc', 'bcc','ltc','eth','lsk','game','dash','btg',
#         'kzc','xin','xrp','zec','gnt','omg','fto','rep',
#         'zrx','pay','bat','neu','trx','amlt','exy','bob']

coinsSmallVer = ['btc','ltc','eth']
for x in range(100):
    for coin in coinsSmallVer:
        requestFormat = 'https://bitbay.net/API/Public/{}/orderbook.json'.format(coin)
        respons = requests.get(requestFormat)
        print("\n"+coin)
        print("bids offers:\t\t\tasks offers:")
        for i in range(5):
            print(str(respons.json()["bids"][i][0])+"\t\t\t\t"+str(respons.json()["asks"][i][0]))
    print("\n\n\n")
    time.sleep(5)