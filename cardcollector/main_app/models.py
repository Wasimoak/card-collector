from django.db import models
from django.urls import reverse
from datetime import date

SALES = (
    ('S', 'Sold'),
    ('B', 'Bought'),
    ('T', 'Trade')
)

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    value = models.TextField(max_length=15)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})

    def buy_for_today(self):
        return self.buying_set.filter(date=date.today()).count() >= len(SALES)

class Buying(models.Model):
  date = models.DateField('buy/sold date')
  sale = models.CharField(
    max_length=1,
    choices=SALES,
    default=SALES[0][0]
  )
  card = models.ForeignKey(Card, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_sale_display()} on {self.date}"


  class Meta:
    ordering = ['-date']