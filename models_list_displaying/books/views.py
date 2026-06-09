from django.shortcuts import render
from books.models import Book
# from django.core.paginator import Paginator
from datetime import datetime

def books_view(request):
    template = 'books/books_db.html'
    books = Book.objects.all().order_by('pub_date') # сортируем по дате

    context = {'books': books}
    return render(request, template, context)


def book_one(request, pub_date):
    template = 'books/books_db.html'
    
    # Преобразуем строку из URL в датУ
    current_date = datetime.strptime(pub_date, '%Y-%m-%d').date()

    # Получаем книги за текущую дату
    books_current = Book.objects.filter(pub_date=current_date).order_by('name')

    # Получаем все уникальные даты из базы данных, сортирУЕМ по возрастанию
    all_dates = Book.objects.values_list('pub_date', flat=True).distinct().order_by('pub_date')
    all_dates_list = list(all_dates)


    # Находим индекс текущей даты в списке всех дат
    prev_date = None
    next_date = None
    
    if current_date in all_dates_list:
        index = all_dates_list.index(current_date)
        
        # Предыдущая дата (если есть)
        if index > 0:
            prev_date = all_dates_list[index - 1]
        
        # Следующая дата (если есть)
        if index < len(all_dates_list) - 1:
            next_date = all_dates_list[index + 1]
    
    context = {
        'books': books_current,
        'current_date': current_date,
        'prev_date': prev_date,
        'next_date': next_date,
    }

    return render(request, template, context)
    
