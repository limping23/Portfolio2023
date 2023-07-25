from django.shortcuts import render


def about(request):
    return render(request, 'main/about.html')


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['some', 'hello']
    }
    return render(request, 'main/index.html', data)


def myprojects(request):
    return render(request, 'main/myprojects.html')
