from django.conf.urls import url
from . import views
from .views import home,cart_add,cart_remove

app_name = 'Calculator'

urlpatterns = [
    url(r'^$',views.home, name='Calculator-home'),
    url(r'^add/(?P<food_id>\d+)/$',views.cart_add,name= 'cart_add'),
    url(r'^remove/(?P<food_id>\d+)/$',views.cart_remove,name='cart_remove'),
]
