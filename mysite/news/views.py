from django.shortcuts import render
from django.http import HttpResponse

from .models import News

# render: request, название шаблона, контекст (если его много, можно создать отдельную переменную)


def index(request):
    news = News.objects.order_by('-created_at')
    context = {'news': news, 'title': 'Список новостей'}
    return render(request, 'news/index.html', context=context)


