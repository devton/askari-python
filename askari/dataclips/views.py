# Create your views here.
from django.views.generic import CreateView, DetailView
from .forms import ClipForm
from .models import Clip


class ClipCreateView(CreateView):
    model = Clip
    form_class = ClipForm


class ClipDetailView(DetailView):
    model = Clip
