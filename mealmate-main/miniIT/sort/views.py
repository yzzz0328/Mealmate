from django.shortcuts import render, redirect, get_object_or_404
from database.models import foodinfo
from .forms import SortFoodForm
from .filters import FoodFilter
from django.views.generic import DetailView

# Create your views here.
# This creates the view for the database 
def index(request):
    return render(request,"index.html")

# This function makes the allows the filtering/ search and the food data to be shown in the database
def display_sortfoods(request):
    name = foodinfo.objects.all()
    myFilter = FoodFilter(request.GET, queryset=name )
    name = myFilter.qs
    context = {
        'name' : name,
        'myFilter': myFilter,
        'header': 'Foods',
        

     }
    
    return render(request, 'index.html', context)

# This creates the deatied view for each of the foods in the database
class browseinfoDetailView(DetailView): 
    model = foodinfo
    template_name = "browseinfo_detail.html"

