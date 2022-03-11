from django.shortcuts import render


def home(request):
    return render(request, 'myproject/home.html')
