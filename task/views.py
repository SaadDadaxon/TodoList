from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, 'task/index.html', context)
