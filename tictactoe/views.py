from django.shortcuts import render
from . import gameplay
def index(request):
    context={
        "board" : gameplay.display_board(),
    }
    return render(request, "home.html", context)

def index2(request):
    return render(request, 'home2.html')

# Create your views here.
