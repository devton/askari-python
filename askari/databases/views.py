# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse
from .models import Database
from .forms import DatabaseForm


class DefaultDatabaseMethods(object):
    form_class = DatabaseForm

    def get_success_url(self):
        return reverse('databases:list')


class DatabaseCreateView(CreateView, DefaultDatabaseMethods):
    template_name = 'databases/database_form.html'


class DatabaseUpdateView(UpdateView, DefaultDatabaseMethods):

    def get_object(self, queryset=None):
        return Database.objects.get(pk=self.kwargs.get('object_id'))


class DatabaseListView(ListView):
    model = Database
    template_name = 'databases/database_list.html'

