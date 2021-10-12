from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv('apikey')


#def news(request):
 #   return HttpResponse("<h4>То шо новости</h4>")


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



