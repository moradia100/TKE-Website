from django.shortcuts import render
from django.views.generic import ListView
from .models import Event

# Create your views here.
from django.http import HttpResponse

# Built-in Django CreateView
from django.views.generic import ListView, CreateView 

#Handle the redirect back to our homepage 
from django.urls import reverse_lazy 

from .forms import EventForm 



# def index(request):
#     context = {
#         "variable":"App",
#         "title":"TKE",
#     }
#     return render(request, "sections/philanthropy.html", context=context)

# A page representing a list of objects.
class EventView(ListView):
    model = Event
    template_name = 'sections/philanthropy.html'

class CreateEventView(CreateView): 
    model = Event
    form_class = EventForm
    template_name = 'sections/post.html'
    success_url = reverse_lazy('philanthropy')