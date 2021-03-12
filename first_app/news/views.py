from django.shortcuts import render
from django.http import HttpResponse, Http404
from news.models import News


# Create your views here.

def index(request, *args, **kwargs):
    qs = News.objects.all()
    context = {'news_list': qs}
    return render(request, 'index.html', context)

def detail_view(request, pk):
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404

    print(request.POST)
    print(request.GET)
    print(request.method == 'POST')
    print(request.method == 'GET')

    return render(request, 'news/detail.html', {'single_object': obj})

def test_view(request, *args, **kwargs):
    data = dict(request.GET)
    print(data)
    obj = News.objects.get(id=data['pk'][0])
    return HttpResponse(f'<b>{obj.article}</b>')

def create_view(request, *args, **kwargs):

    if request.method == 'POST':
        data = request.POST
        article = data['article']
        body = data['body']
        key = ['', ' ']
        if article not in key and body not in key:
            News.objects.create(article=article, body=body)

    print(request.POST)
    print(request.GET)
    return render(request, 'forms.html')