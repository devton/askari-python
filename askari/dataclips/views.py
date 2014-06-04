from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
from ..core.mixins import LoginRequiredViewMixin, GenericTemplateDataMixin
from .forms import ClipForm
from .models import Clip


class ClipMixin(GenericTemplateDataMixin, LoginRequiredViewMixin):
    model = Clip

    def get_queryset(self):
        qs = super(ClipMixin, self).get_queryset()
        return qs & Clip.objects.filter(database__user__pk=self.request.user.pk)


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

    def get_context_data(self, **kwargs):
        context = super(ClipUpdateView, self).get_context_data(**kwargs)

        try:
            executed_sql = self.object.exec_query()
        except Exception as error:
            executed_sql = None
            messages.add_message(self.request, messages.ERROR, "{}".format(error))

        context_data = {'sql_exec': executed_sql}

        context.update(context_data)
        return context



class ClipDeleteView(ClipFormMixin, DeleteView):
    def get_success_url(self):
        return reverse('dataclips:list')


class ClipPublicView(DetailView):
    model = Clip
    template_name = "dataclips/clip_public.html"