from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime, os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    
    # так не интеренсо "просто текст", сделал с возращением на главную страницу
    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    html = f'''
    <h1>Текущее время: {current_time}</h1>
    <br>
    <a href="/">Вернуться на главную</a>
    '''
    return HttpResponse(html)

def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    catalog = os.listdir('.')
    result = ''.join([f'<li>{item}</li>' for item in catalog])
    html = f'''
    <h1>Содержимое директории:</h1>
    <ul>{result}</ul>
    <br>
    <a href="/">Вернуться на главную</a>
    '''
    return HttpResponse(html)
