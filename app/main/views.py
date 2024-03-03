from django.shortcuts import render

from main.models import Insurance

# Create your views here.


def index(request):
    context = {
        'insurance': Insurance.objects.all(),
    }
    return render(request, 'main/index.html', context)

