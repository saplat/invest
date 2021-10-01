from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def news(request):
 #   return HttpResponse("<h4>То шо новости</h4>")
def news(request):
    return render(request, 'main/news.html')


def index(request):
    return render(request, 'main/index.html')
