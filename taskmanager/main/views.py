from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
import time
import asyncio
import websockets
import queue
from dotenv import load_dotenv
from yahoo_fin.stock_info import *
from threading import Thread

load_dotenv()
apikey = os.getenv('apikey')


#def news(request):
 #   return HttpResponse("<h4>То шо новости</h4>")


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
