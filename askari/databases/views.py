# Create your views here.
from django.views.generic import CreateView
from askari.databases.models import Database


class DatabaseCreateView(CreateView):
    model = Database
