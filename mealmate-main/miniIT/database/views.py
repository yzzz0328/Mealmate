from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import addfoodform
from .models import foodinfo
from django.views.generic import DetailView,UpdateView
from django.urls import reverse
from django import forms

# Add food function
def home(request):    
              
    if request.method == 'POST':
        addfood = addfoodform(request.POST)
        if addfood.is_valid(): # Checks if addfoodform is valid with no errors
            addfood.save() # Adds new food into database
            foodname = addfood.cleaned_data.get('name')
            messages.success(request, f'{foodname} has been added into the database!') # Create success message with new food's name
            return redirect('database-home')
    else:
        addfood = addfoodform()
        context = { # Context for template to load
            'foodform': addfood,
            'foods' : foodinfo.objects.all(),
            'title' : "Food Editor"
        }
    return render(request, 'database/home.html', context)

# Food Detail
class foodinfoDetailView(DetailView): 
    model = foodinfo

# Edit Food function
class foodinfoUpdateView(UpdateView):
    model = foodinfo

    #Fields that the user can edit the value
    fields = [ 
            'name',
            'description',
            'mealtype',
            'calories',
            'carbs',
            'protein',
            'fat',
            'fibre',
            'size',
        ]

# Delete food function
def foodinfo_delete(request,pk):
    
    #Deletes the object with the id of pk from the database
    foodinfo.objects.filter(id=pk).delete() 
    
    return redirect('database-home')