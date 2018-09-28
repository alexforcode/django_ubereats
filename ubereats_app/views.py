from django.shortcuts import render


def index(request):
    return render(request, 'ubereats_app/index.html', {})
