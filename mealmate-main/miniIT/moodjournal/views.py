from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView
)
from .models import Entry
from .forms import EntryForm
from .filters import EntryFilter

# Viewing the homepage, it obtains all entries from the database.
def home(request):
    context = {
        'entry': Entry.objects.all()
    }
    return render(request, 'moodjournal/home.html', context)


class EntryListView(ListView):
    model = Entry
    template_name = 'moodjournal/home.html'  # <app>/<model>_<viewtype>
    context_object_name = 'entries'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EntryFilter(self.request.GET, queryset=self.get_queryset())
        return context


class EntryDetailView(DetailView):
    model = Entry


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = '/moodjournal'


def about(request):
    return render(request, 'moodjournal/about.html', {'title': 'About'})


def EntryCreateView(request):
    entries = Entry.objects.all()
    form = EntryForm()

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry is posted!')
            return redirect('moodjournal-home')
    else:
        form = EntryForm()

    context = {'entries': entries, 'form': form, 'title':'Create Entry'}
    return render(request, 'moodjournal/entry_form.html', context)


def EntryUpdateView(request, pk):
    entry = Entry.objects.get(id=pk)
    form = EntryForm(instance=entry)

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, f'Entry is updated!')
            return redirect('moodjournal-home')

    context = {'form': form, 'title':'Update Entry'}
    return render(request, 'moodjournal/entry_update.html', context)
    