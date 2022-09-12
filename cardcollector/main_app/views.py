from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Card:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, sport, description, value):
    self.name = name
    self.sport = sport
    self.description = description
    self.value = value

cards = [
  Card('Lebron JAmes', 'basketball', '2019 Panini Prizm Lebron James Green Prizm PSA 10', '$40'),
  Card('Wayne Gretzky', 'hockey', '1995-96 ultra gold medallion wayne gretzky #74', '$80'),
  Card('Jackie Robinson', 'baseball', '1956 Topps # 30 Jackie Robinson Gray Back', '$90')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello CARD COLLECTOR</h1>')

def about(request):
  return render(request, 'about.html')

def cards_index(request):
  return render(request, 'cards/index.html', { 'cards': cards })