# Generated by Django 4.1.1 on 2022-09-14 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sale', models.CharField(choices=[('S', 'Sold'), ('B', 'Bought'), ('T', 'Trade')], default='S', max_length=1)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.card')),
            ],
        ),
    ]
