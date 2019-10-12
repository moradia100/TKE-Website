from django.urls import path, include
from . import views
from . import philan

urlpatterns = [
		path('', views.index),
		path('philanthropy/', philan.index),
]