# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from .models import Database
from .forms import DatabaseForm


class DatabaseMixin(object):
    model = Database


class DatabaseFormMixin(DatabaseMixin):
    form_class = DatabaseForm

    def get_success_url(self):
        return reverse('databases:list')


class DatabaseCreateView(DatabaseFormMixin, CreateView):
    pass


class DatabaseUpdateView(DatabaseFormMixin, UpdateView):
    pass


class DatabaseListView(DatabaseMixin, ListView):
    pass


class DatabaseDeleteView(DatabaseFormMixin, DeleteView):
    pass

