from django.shortcuts import render,redirect,get_object_or_404
from database.models import foodinfo
from .forms import ChooseFoodForm,CartAddFoodForm
from .filters import foodFilter
from .cart import Cart
from django.views.decorators.http import require_POST

# Create your views here.

def home(request):
    cart = Cart(request)
    cart_form = CartAddFoodForm()
    name = foodinfo.objects.all()
    myFilter = foodFilter(request.GET, queryset=name)
    name = myFilter.qs
     
    context = {
        'name' : name,
        'myFilter': myFilter,
        'cart_form' : cart_form,
        'cart' : cart,
    }

    return render(request,"Calculator/calculator.html",context)

# add food into cart
def cart_add(request,food_id):
    if request.method == 'POST':
        cart = Cart(request)
        food = get_object_or_404(foodinfo, id=food_id)
        form = CartAddFoodForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(foodinfo=food,
                    quantity=cd['quantity'],
                    update_quantity=cd['update'])
        return redirect('Calculator:Calculator-home')

#remove food from cart
def cart_remove(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(foodinfo, id=food_id)
    cart.remove(food)
    return redirect('Calculator:Calculator-home')

