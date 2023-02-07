from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError

# Create your views here.
def mainShow(request):
    return HttpResponse("Hello World")

def categories(request, catid):
    return HttpResponse(f"<h1>Hello on my first page</h1> <p>{catid}</p>")

def archive(request, year):
    if int(year)>2023:
        return redirect('home ',permanent=False)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound (request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def badGateWay (request, exception):
    return HttpResponseBadRequest('<h1>Ошибка</h1>')

def serverError (request,  *args, **argv):
    return (request, '300.html', status:=500)

