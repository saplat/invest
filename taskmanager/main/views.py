import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.exceptions import ConnectionError
import os
import time
import asyncio
import websockets
import queue
from dotenv import load_dotenv
from yahoo_fin.stock_info import *
from threading import Thread
from bs4 import BeautifulSoup
from .lifestockfunc import Lifestockfunc

load_dotenv()
apikey = os.getenv('apikey')


#def news(request):
 #   return HttpResponse("<h4>То шо новости</h4>")


def lifestocks(request):
        url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
        try:
            r = requests.get(url)
            web_content = BeautifulSoup(r.text, 'lxml')
            texts = Lifestockfunc.web_content_div(web_content, 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)')
            if texts != []:
                print(texts)
                price, change, times = texts[0], texts[1], texts[2]
            else:
                price, change = [], []
        except ConnectionError:
            price, change = [], []

        try:
            r = requests.get(url)
            web_content = BeautifulSoup(r.text, 'lxml')
            texts = Lifestockfunc.web_content_div(web_content, 'Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)')
            if texts != []:
                print(texts)
                price1, change1, times1 = texts[0], texts[2], texts[3]
            else:
                price1, change1 = [], []
        except ConnectionError:
            price1, change1 = [], []

        context = {'price' : price,
                   'change' : change,
                   'times' : times,
                   'price1' : price1,
                   'change1' : change1,
                   'times1' : times1}
        return render(request, 'main/lifestocks.html', context)

def lifestocks1(request):
    #while(True):
        lifestocks(request)
        time.sleep(60)


def layout(request):
    data = get_currencies()
    EURUSD = {'name':data._get_value(0,'Name'),
              'LP': data._get_value(0,'Last Price'),
              'change': data._get_value(0, '% Change')}

    USDRUB = {'name':data._get_value(23,'Name'),
              'LP': data._get_value(23,'Last Price'),
              'change': data._get_value(23, '% Change')}

    USDJPY = {'name':data._get_value(1,'Name'),
              'LP': data._get_value(1,'Last Price'),
              'change': data._get_value(1, '% Change')}

    GBPUSD = {'name':data._get_value(2,'Name'),
              'LP': data._get_value(2,'Last Price'),
              'change': data._get_value(2, '% Change')}

    currencies = {'EURUSD': EURUSD,
                  'USDRUB': USDRUB,
                  'USDJPY': USDJPY,
                  'GBPUSD': GBPUSD}

    context = {'currencies': currencies}
    return render(request, 'main/layout.html', context)


def index(request):
    return render(request, 'main/index.html')


def news(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={apikey}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']

    context = {
        'articles':articles
    }
    return render(request, 'main/news.html', context)


def stockPicker(request):
    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request, 'main/stockpicker.html', {'stockpicker':stock_picker})


def stockTracker(request):
    stockpicker = request.GET.getlist('stockpicker')
    print(stockpicker)
    data = {}
    available_stocks = tickers_nifty50()
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")

    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()
    start = time.time()
    #for i in stockpicker:
    #    result = get_quote_table(i)
    #    data.update({i : result})
    for i in range(n_threads):
        thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]: get_quote_table(arg1)}), args = (que, stockpicker[i]))
        thread_list.append(thread)
        thread_list[i].start()
    for thread in thread_list:
        thread.join()
    while not que.empty():
        result = que.get()
        data.update(result)
    end = time.time()
    time_takem = end - start
    print(time_takem)
    print (data)
    return render(request, 'main/stockTracker.html', {'data' : data})
