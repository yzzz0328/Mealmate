from django.urls import path
from . import views
from mealmate.views import mealplan

urlpatterns = [
    path('', mealplan.as_view(), name= 'mealmate-mealplan'),
]
