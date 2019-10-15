from django.urls import path, include
from . import views
from . import philan



urlpatterns = [
		path('', views.index),
		#path('philanthropy/', philan.index),
		path('philanthropy/', philan.EventView.as_view(), name='philanthropy'),
		path('post/', philan.CreateEventView.as_view()),
]