import asyncio
import os
import queue
import time
from threading import Thread

import pandas as pd
import requests
import websockets
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv
from requests.exceptions import ConnectionError
from yahoo_fin.stock_info import *

from .lifestockfunc import Lifestockfunc

load_dotenv()
apikey = os.getenv('apikey')


#def news(request):
 #   return HttpResponse("<h4>То шо новости</h4>")

def graph(request):
    return render(request, "main/graph.html", context={'text' : 'Hello world'})

def AAPL(request):
        url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
        try:
            r = requests.get(url)
            web_content = BeautifulSoup(r.text, 'lxml')
            texts = Lifestockfunc.web_content_div(web_content, 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)')
            if texts != []:
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
                price1, change1, times1 = texts[0], texts[2], texts[3]
            else:
                price1, change1, times1 = [], [], []
        except ConnectionError:
            price1, change1, times1 = [], [], []

        try:
            r = requests.get(url)
            web_content = BeautifulSoup(r.text, 'lxml')
            texts = Lifestockfunc.web_content_div(web_content, 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
            print(texts)
            if texts != []:
                #previous_close, open, bid, ask, volume, avgvolume = texts[1], texts[3], texts[5], texts[7], texts[11], texts[13]
                previous_close, open, bid, ask, volume, avgvolume = texts[1], texts[3], texts[5], texts[7], texts[9], texts[11]
            else:
                previous_close, open, bid, ask, volume, avgvolume = [], [], [], [], [], []
        except ConnectionError:
            previous_close, open, bid, ask, volume, avgvolume = [], [], [], [], [], []

        try:
            r = requests.get(url)
            web_content = BeautifulSoup(r.text, 'lxml')
            texts = Lifestockfunc.web_content_div_td(web_content, 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
            if texts != []:
                days_range, week_range = texts[9], texts [11]
            else:
                days_range, week_range = [], []
        except ConnectionError:
            days_range, week_range = [], []



        try:
            r = requests.get(url)
            web_content = BeautifulSoup(r.text, 'lxml')
            texts = Lifestockfunc.web_content_div_td(web_content, 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)')
            if texts != []:
                market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = texts[1], texts[3], texts[5], texts[7], texts[9], texts[11], texts[13], texts[15]
            else:
                market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = [], [], [], [], [], [], [], []
        except ConnectionError:
            market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = [], [], [], [], [], [], [], []

        context = {'price' : price,
                   'change' : change,
                   'times' : times,
                   'price1' : price1,
                   'change1' : change1,
                   'times1' : times1,
                   'previous_close': previous_close,
                   'open' : open,
                   #'bid' : bid,
                   #'ask' : ask,
                   'volume' : volume,
                   'avgvolume' : avgvolume,
                   'days_range' : days_range,
                   'week_range' : week_range,
                   'market_cap' : market_cap,
                   'beta' : beta,
                   'pe_ratio' : pe_ratio,
                   'epc' : epc,
                   'earn_date' : earn_date,
                   'forward_div' : forward_div,
                   'ex_div' : ex_div,
                   'target_est' : target_est}
        return render(request, 'main/aapl.html', context)


def AMZN(request):
    url = 'https://finance.yahoo.com/quote/AMZN?p=AMZN&ncid=stockrec'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content, 'My(6px) Pos(r) smartphone_Mt(6px) W(100%)')
        if texts != []:
            price, change, times = texts[0], texts[1], texts[2]
        else:
            price, change, times = [], [], []
    except ConnectionError:
        price, change, times = [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content, 'Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)')
        if texts != []:
            price1, change1, times1 = texts[0], texts[2], texts[3]
        else:
            price1, change1, times1 = [], [], []
    except ConnectionError:
        price1, change1, times1 = [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content,
                                              'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
        if texts != []:
            previous_close, open, bid, ask, volume, avgvolume = texts[1], texts[3], texts[5], texts[7], texts[11], \
                                                                texts[13]
        else:
            previous_close, open, bid, ask, volume, avgvolume = [], [], [], [], [], []
    except ConnectionError:
        previous_close, open, bid, ask, volume, avgvolume = [], [], [], [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div_td(web_content,
                                                 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
        if texts != []:
            days_range, week_range = texts[9], texts[11]
        else:
            days_range, week_range = [], []
    except ConnectionError:
        days_range, week_range = [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div_td(web_content,
                                                 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)')
        if texts != []:
            market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = texts[1], texts[3], texts[5], \
                                                                                          texts[7], texts[9], texts[11], \
                                                                                          texts[13], texts[15]
        else:
            market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = [], [], [], [], [], [], [], []
    except ConnectionError:
        market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = [], [], [], [], [], [], [], []

    context = {'price': price,
               'change': change,
               'times': times,
               'price1': price1,
               'change1': change1,
               'times1': times1,
               'previous_close': previous_close,
               'open': open,
               'bid': bid,
               'ask': ask,
               'volume': volume,
               'avgvolume': avgvolume,
               'days_range': days_range,
               'week_range': week_range,
               'market_cap': market_cap,
               'beta': beta,
               'pe_ratio': pe_ratio,
               'epc': epc,
               'earn_date': earn_date,
               'forward_div': forward_div,
               'ex_div': ex_div,
               'target_est': target_est}
    return render(request, 'main/amzn.html', context)

def GOOG(request):
    url = 'https://finance.yahoo.com/quote/GOOG?p=GOOG&ncid=stockrec'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content, 'D(ib) Va(m) Maw(65%) Ov(h)')
        if texts != []:
            price, change, times = texts[0], texts[1], texts[2]
        else:
            price, change, times = [], [], []
    except ConnectionError:
        price, change, times = [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content, 'Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)')
        if texts != []:
            price1, change1, times1 = texts[0], texts[2], texts[3]
        else:
            price1, change1, times1 = [], [], []
    except ConnectionError:
        price1, change1, times1 = [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content,
                                              'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
        if texts != []:
            previous_close, open, bid, ask, volume, avgvolume = texts[1], texts[3], texts[5], texts[7], texts[11], \
                                                                texts[13]
        else:
            previous_close, open, bid, ask, volume, avgvolume = [], [], [], [], [], []
    except ConnectionError:
        previous_close, open, bid, ask, volume, avgvolume = [], [], [], [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div_td(web_content,
                                                 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
        if texts != []:
            days_range, week_range = texts[9], texts[11]
        else:
            days_range, week_range = [], []
    except ConnectionError:
        days_range, week_range = [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div_td(web_content,
                                                 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)')
        if texts != []:
            market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = texts[1], texts[3], texts[5], \
                                                                                          texts[7], texts[9], texts[11], \
                                                                                          texts[13], texts[15]
        else:
            market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = [], [], [], [], [], [], [], []
    except ConnectionError:
        market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = [], [], [], [], [], [], [], []

    context = {'price': price,
               'change': change,
               'times': times,
               'price1': price1,
               'change1': change1,
               'times1': times1,
               'previous_close': previous_close,
               'open': open,
               'bid': bid,
               'ask': ask,
               'volume': volume,
               'avgvolume': avgvolume,
               'days_range': days_range,
               'week_range': week_range,
               'market_cap': market_cap,
               'beta': beta,
               'pe_ratio': pe_ratio,
               'epc': epc,
               'earn_date': earn_date,
               'forward_div': forward_div,
               'ex_div': ex_div,
               'target_est': target_est}
    return render(request, 'main/goog.html', context)


def FB(request):
    url = 'https://finance.yahoo.com/quote/FB?p=FB&ncid=stockrec'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content, 'D(ib) Va(m) Maw(65%) Ov(h)')
        if texts != []:
            price, change, times = texts[0], texts[1], texts[2]
        else:
            price, change, times = [], [], []
    except ConnectionError:
        price, change, times = [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content, 'Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)')
        if texts != []:
            price1, change1, times1 = texts[0], texts[2], texts[3]
        else:
            price1, change1, times1 = [], [], []
    except ConnectionError:
        price1, change1, times1 = [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div(web_content,
                                              'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
        if texts != []:
            previous_close, open, bid, ask, volume, avgvolume = texts[1], texts[3], texts[5], texts[7], texts[11], \
                                                                texts[13]
        else:
            previous_close, open, bid, ask, volume, avgvolume = [], [], [], [], [], []
    except ConnectionError:
        previous_close, open, bid, ask, volume, avgvolume = [], [], [], [], [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div_td(web_content,
                                                 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
        if texts != []:
            days_range, week_range = texts[9], texts[11]
        else:
            days_range, week_range = [], []
    except ConnectionError:
        days_range, week_range = [], []

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = Lifestockfunc.web_content_div_td(web_content,
                                                 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)')
        if texts != []:
            market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = texts[1], texts[3], texts[5], \
                                                                                          texts[7], texts[9], texts[11], \
                                                                                          texts[13], texts[15]
        else:
            market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = [], [], [], [], [], [], [], []
    except ConnectionError:
        market_cap, beta, pe_ratio, epc, earn_date, forward_div, ex_div, target_est = [], [], [], [], [], [], [], []

    context = {'price': price,
               'change': change,
               'times': times,
               'price1': price1,
               'change1': change1,
               'times1': times1,
               'previous_close': previous_close,
               'open': open,
               'bid': bid,
               'ask': ask,
               'volume': volume,
               'avgvolume': avgvolume,
               'days_range': days_range,
               'week_range': week_range,
               'market_cap': market_cap,
               'beta': beta,
               'pe_ratio': pe_ratio,
               'epc': epc,
               'earn_date': earn_date,
               'forward_div': forward_div,
               'ex_div': ex_div,
               'target_est': target_est}
    return render(request, 'main/fb.html', context)





#def lifestocks1(request):
#    print('AAAAAAAAAAAAAAAAAAAAAAAAAAA')
#    while(True):
#        lifestocks(request)
#        time.sleep(30)
#    return render(request, 'main/aapl.html')


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

    data = get_currencies()
    EURUSD = {'name': data._get_value(0, 'Name'),
              'LP': data._get_value(0, 'Last Price'),
              'change': data._get_value(0, '% Change')}

    USDRUB = {'name': data._get_value(23, 'Name'),
              'LP': data._get_value(23, 'Last Price'),
              'change': data._get_value(23, '% Change')}

    USDJPY = {'name': data._get_value(1, 'Name'),
              'LP': data._get_value(1, 'Last Price'),
              'change': data._get_value(1, '% Change')}

    GBPUSD = {'name': data._get_value(2, 'Name'),
              'LP': data._get_value(2, 'Last Price'),
              'change': data._get_value(2, '% Change')}

    context = {
        'articles':articles,
        'EURUSD': EURUSD,
        'USDRUB': USDRUB,
        'USDJPY': USDJPY,
        'GBPUSD': GBPUSD
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
