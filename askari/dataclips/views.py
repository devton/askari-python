from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from .forms import ClipForm
from .models import Clip


class ClipMixin(object):
    model = Clip

    def get_queryset(self):
        qs = super(ClipMixin, self).get_queryset()
        return qs & self.request.user.clips()


class ClipFormMixin(ClipMixin):
    form_class = ClipForm

    def get_success_url(self):
        return reverse('dataclips:edit', kwargs={'pk': self.object.pk})


class ClipListView(ClipMixin, ListView):
    pass


class ClipCreateView(ClipFormMixin, CreateView):
    pass


class ClipUpdateView(ClipFormMixin, UpdateView):
    template_name = "dataclips/clip_update_and_show.html"


class ClipDeleteView(ClipFormMixin, DeleteView):
    def get_success_url(self):
        return reverse('dataclips:list')