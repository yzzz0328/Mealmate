from django.db import models
from django import forms
from django.urls import reverse

class foodinfo(models.Model):

    mealtype_choices = (
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
    )

    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    mealtype = models.CharField(max_length=300,blank=True,choices=mealtype_choices)
    calories = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    fibre = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return self.name

    # Goes back to food's info page after being edited succesfully
    def get_absolute_url(self): 
        return reverse('foodinfo-detail', kwargs={'pk': self.pk})

