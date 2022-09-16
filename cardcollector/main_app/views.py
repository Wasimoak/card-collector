from django.shortcuts import render, redirect
from .models import Card, Grade
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import BuyingForm

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cards_index(request):
  cards = Card.objects.all()
  return render(request, 'cards/index.html', { 'cards': cards })

def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  buying_form = BuyingForm()
  return render(request, 'cards/detail.html', { 
    'card': card, 
    'buying_form': buying_form
    })
  
class CardCreate(CreateView):
  model = Card
  fields = '__all__'

class CardUpdate(UpdateView):
  model = Card
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name','sport', 'description', 'value']

class CardDelete(DeleteView):
  model = Card
  success_url = '/cards/'

def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  grades_card_doesnt_have = Grade.objects.exclude(id__in = card.grades.all().values_list('id'))
  buying_form = BuyingForm()
  return render(request, 'cards/detail.html', {
    'card': card, 'buying_form': buying_form,
    'grades': grades_card_doesnt_have
  })

def add_buying(request, card_id):
  form = BuyingForm(request.POST)
  if form.is_valid():
    new_buying = form.save(commit=False)
    new_buying.card_id = card_id
    new_buying.save()
  return redirect('detail', card_id=card_id)

def assoc_grade(request, card_id, grade_id):
  Card.objects.get(id=card_id).grades.add(grade_id)
  return redirect('detail', card_id=card_id)

def unassoc_grade(request, card_id, grade_id):
  Card.objects.get(id=card_id).grades.remove(grade_id)
  return redirect('detail', card_id=card_id)


class GradeList(ListView):
  model = Grade

class GradeDetail(DetailView):
  model = Grade

class GradeCreate(CreateView):
  model = Grade
  fields = '__all__'

class GradeUpdate(UpdateView):
  model = Grade
  fields = ['name', 'color']

class GradeDelete(DeleteView):
  model = Grade
  success_url = '/grades/'


