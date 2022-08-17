import pyupbit
import time
from statistics import mean
from datetime   import datetime
#테스트 케이스
money   = 100000
coin    = 0
ticker  = "KRW-ETC"

def get_ma():
    arr  = []
    for i in range(10):
        arr.append(past_price.iloc[i]['close'])
    res = mean(arr)
    return res

def yester_low():
    res1 = yesterday.iloc[0]['low']
    return res1

def current_day():
    ct = datetime.now()
    day = ct.day
    return day

def current_minute():
    ct = datetime.now()
    minute = ct.minute
    return minute

def test():
    res2 = (yesterday.iloc[0]['high']-yesterday.iloc[0]['low'])*0.5
    return res2

#초기화
current_time = datetime.now()
past_price   = pyupbit.get_ohlcv(ticker=ticker, interval='minute1', count=10) 
yesterday    = pyupbit.get_ohlcv(ticker=ticker, interval='day', count=2)
ma = get_ma()
buy_point = 0

while True:
    if current_time.day != current_day():
        current_time = datetime.now()
        yesterday    = pyupbit.get_ohlcv(ticker=ticker, interval='day', count=2)
    if current_time.minute != current_minute():
        current_time = datetime.now()
        past_price   = pyupbit.get_ohlcv(ticker=ticker, interval='minute1', count=10) 
        ma = get_ma()
    current_price = pyupbit.get_current_price(ticker)
    if current_price > yester_low():
        if (current_price > ma) and (money >= current_price):
            coin += money//current_price
            money -= coin*current_price
            buy_point = current_price
            print(money,",",coin)
        elif (current_price < ma) and (current_price > buy_point) and (coin > 0):
            money += coin*current_price
            coin = 0
            print(money)
    if money+coin*current_price <= 0:
        print("u screwed up")
        break
    time.sleep(10)
        


