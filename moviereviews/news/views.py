from django.shortcuts import render
from .models import News
def news(request):
    context = {
        'newss': News.objects.all().order_by('-date')
    }
    return render(request, 'news/news.html', context)