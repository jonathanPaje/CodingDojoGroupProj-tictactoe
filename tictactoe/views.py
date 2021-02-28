from django.shortcuts import render
from . import gameplay
def index(request):
    context={
        "board" : gameplay.display_board()
    }
    return render(request, "home.html", context)

# Create your views here.
