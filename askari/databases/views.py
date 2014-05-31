# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from ..core.views import LoginRequiredViewMixin
from .models import Database
from .forms import DatabaseForm


class DatabaseMixin(LoginRequiredViewMixin):
    model = Database

    def get_queryset(self):
        qs = super(DatabaseMixin, self).get_queryset()
        return qs & self.request.user.databases()


class DatabaseFormMixin(DatabaseMixin):
    form_class = DatabaseForm

    def get_success_url(self):
        return reverse('databases:list')


class DatabaseCreateView(DatabaseFormMixin, CreateView):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DatabaseCreateView, self).form_valid(form)


class DatabaseUpdateView(DatabaseFormMixin, UpdateView):
    pass


class DatabaseListView(DatabaseMixin, ListView):
    pass


class DatabaseDeleteView(DatabaseFormMixin, DeleteView):
    pass

