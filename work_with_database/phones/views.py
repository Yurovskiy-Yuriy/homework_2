from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')
 

def show_catalog(request):
    template = 'catalog.html'

    phones = Phone.objects.all()

    # сортировка
    sort_param = request.GET.get('sort')
    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    # slug=slug ищем телефон, у которого поле slug равно значению из URL
    phone = Phone.objects.get(slug=slug)
    
    context = {'phone': phone}
    return render(request, template, context)
