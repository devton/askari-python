# Create your views here.
from django.views.generic import CreateView, ListView
from .models import Database
from .forms import DatabaseForm


class DatabaseCreateView(CreateView):
    model = Database
    form = DatabaseForm
    template_name = 'databases/database_form.html'


class DatabaseListView(ListView):
    model = Database
    template_name = 'databases/database_list.html'

