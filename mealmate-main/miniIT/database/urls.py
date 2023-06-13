from django.urls import path
from . import views
from .views import foodinfoDetailView,foodinfoUpdateView,foodinfo_delete

urlpatterns = [
    path('', views.home, name='database-home'), # Links to food editor's main page
    path('<pk>/', foodinfoDetailView.as_view(), name='foodinfo-detail'), # links to food's detail page
    path('<pk>/edit/', foodinfoUpdateView.as_view(), name='foodinfo-edit'), # links to food's edit page
    path('<pk>/delete/', views.foodinfo_delete,name='foodinfo-delete'), # Links to delete food function
    ]
