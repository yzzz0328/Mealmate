from django.urls import path
from .views import (
    EntryListView,
    EntryDetailView,
    EntryDeleteView
)
from . import views

urlpatterns = [
    path('', EntryListView.as_view(), name='moodjournal-home'), # The homepage of moodjournal
    path('about/', views.about, name='moodjournal-about'), # The about page of moodjournal
    path('entry/new/', views.EntryCreateView, name='entry-create'), # The page for new entry creation
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'), # User wants to view more details of an existing entry
    path('entry/<int:pk>/update/', views.EntryUpdateView, name='entry-update'), # User wants to update an existing entry
    path('entry/<int:pk>/delete/',EntryDeleteView.as_view(), name='entry-delete'), # User wants to delete an existing entry
]
