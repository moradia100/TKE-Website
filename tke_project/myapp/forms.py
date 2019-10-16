from django import forms
from .models import Event
from .models import Gallery
class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', 'created_date', 'max_volunteers', 'status', 'cover']

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['title', 'Image']
