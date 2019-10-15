from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {
        "variable":"Welcome To TKE Theta-Pi boiiiii",
        "title":"TKE",
    }
    return render(request, "index.html", context=context)
