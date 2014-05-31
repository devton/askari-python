from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from .forms import ClipForm
from .models import Clip


class ClipMixin(object):
    model = Clip

    def get_queryset(self):
      qs = super(ClipMixin, self).get_queryset()
      return qs.filter(database__user_id=self.request.user.pk)



class ClipFormMixin(ClipMixin):
    form_class = ClipForm

    def get_success_url(self):
        return reverse('dataclips:show', kwargs={'pk': self.object.pk})


class ClipListView(ClipMixin, ListView):
    pass


class ClipCreateView(ClipFormMixin, CreateView):
    pass


class ClipDetailView(ClipMixin, DetailView):
    pass


class ClipUpdateView(ClipFormMixin, UpdateView):
    pass


class ClipDeleteView(ClipFormMixin, DeleteView):
    def get_success_url(self):
        return reverse('dataclips:list')

