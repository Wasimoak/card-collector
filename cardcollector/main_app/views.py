from django.shortcuts import render, redirect
from .models import Card, Grade
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import BuyingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def cards_index(request):
  cards = Card.objects.filter(user=request.user)
  return render(request, 'cards/index.html', { 'cards': cards })

@login_required
def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  buying_form = BuyingForm()
  return render(request, 'cards/detail.html', { 
    'card': card, 
    'buying_form': buying_form
    })
  
class CardCreate(LoginRequiredMixin, CreateView):
  model = Card
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
  model = Card
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name','sport', 'description', 'value']

class CardDelete(LoginRequiredMixin, DeleteView):
  model = Card
  success_url = '/cards/'

@login_required
def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  grades_card_doesnt_have = Grade.objects.exclude(id__in = card.grades.all().values_list('id'))
  buying_form = BuyingForm()
  return render(request, 'cards/detail.html', {
    'card': card, 'buying_form': buying_form,
    'grades': grades_card_doesnt_have
  })

@login_required
def add_buying(request, card_id):
  form = BuyingForm(request.POST)
  if form.is_valid():
    new_buying = form.save(commit=False)
    new_buying.card_id = card_id
    new_buying.save()
  return redirect('detail', card_id=card_id)

@login_required
def assoc_grade(request, card_id, grade_id):
  Card.objects.get(id=card_id).grades.add(grade_id)
  return redirect('detail', card_id=card_id)

@login_required
def unassoc_grade(request, card_id, grade_id):
  Card.objects.get(id=card_id).grades.remove(grade_id)
  return redirect('detail', card_id=card_id)


class GradeList(LoginRequiredMixin, ListView):
  model = Grade

class GradeDetail(LoginRequiredMixin, DetailView):
  model = Grade

class GradeCreate(LoginRequiredMixin, CreateView):
  model = Grade
  fields = '__all__'

class GradeUpdate(LoginRequiredMixin, UpdateView):
  model = Grade
  fields = ['name', 'color']

class GradeDelete(LoginRequiredMixin, DeleteView):
  model = Grade
  success_url = '/grades/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
