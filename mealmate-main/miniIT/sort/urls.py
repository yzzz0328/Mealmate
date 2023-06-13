from django.conf.urls import url
from django.urls import path
from .import views
from .views import index, display_sortfoods, browseinfoDetailView



urlpatterns = [
    url(r'^$', index, name='index'), # Opens up database when clicked on browse food
    url(r'^display_sortfoods$', display_sortfoods, name='display_sortfoods'), # Shows overall food data
    url(r'^detail/(?P<pk>\d+)/$', browseinfoDetailView.as_view(), name='browseinfo-detail'), # Detail view of each food 
]
