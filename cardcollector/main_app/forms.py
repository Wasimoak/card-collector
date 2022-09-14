from django.forms import ModelForm
from .models import Buying

class BuyingForm(ModelForm):
  class Meta:
    model = Buying
    fields = ['date', 'sale']