"""miniIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls), # Links to admin page
    path('', include('mealmate.urls')), # Landing page, which is the mealmate module
    path('database/', include('database.urls')), # Links to database module
    path('moodjournal/', include('moodjournal.urls')), # Links to moodjournal module
    path('Calculator/', include(('Calculator.urls','Calculator'),namespace ='Calculator')), # Links to Calorie Calculator module
    path('sort/',include('sort.urls')), # Links to Food Browser module
]
