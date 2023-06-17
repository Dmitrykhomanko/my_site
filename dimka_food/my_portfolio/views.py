from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html', {'title':'Simple Dishes = ГЛАВНАЯ СТРАНИЦА'})


def resume(request):
    return render (request, 'resume.html', {'title':'Мое резюме'})


