from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.contrib import messages
from django.views.generic import (ListView, CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.core.urlresolvers import reverse

from ..core.mixins import LoginRequiredViewMixin, GenericTemplateDataMixin
from .filters import ClipFilter
from .forms import ClipForm
from .models import Clip


@python_2_unicode_compatible
class ClipMixin(GenericTemplateDataMixin, LoginRequiredViewMixin):
    model = Clip

    def get_queryset(self):
        qs = super(ClipMixin, self).get_queryset()
        clips = Clip.objects.filter(organization=self.organization)
        return qs & clips


@python_2_unicode_compatible
class ClipFormMixin(ClipMixin):
    form_class = ClipForm

    def get_success_url(self):
        return reverse('dataclips:edit', kwargs={
            'pk': self.object.pk,
            'organization': self.organization.slug})


@python_2_unicode_compatible
class ClipListView(ClipMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super(ClipListView, self).get_context_data(**kwargs)
        f = ClipFilter(self.request.GET, queryset=self.get_queryset())

        context_data = {'filter': f, 'object_list': f.qs}
        context.update(context_data)

        return context


@python_2_unicode_compatible
class ClipCreateView(ClipFormMixin, CreateView):
    pass


@python_2_unicode_compatible
class ClipUpdateView(ClipFormMixin, UpdateView):
    template_name = "dataclips/clip_update_and_show.html"

    def get_context_data(self, **kwargs):
        context = super(ClipUpdateView, self).get_context_data(**kwargs)

        executed_sql = self.object.query_result()
        try:
            executed_sql = self.object.query_result()
        except Exception as error:
            executed_sql = None
            messages.add_message(self.request, 
                                 messages.ERROR, 
                                 "{}".format(error))

        context_data = {'sql_exec': executed_sql}

        context.update(context_data)
        return context


class ClipDeleteView(ClipFormMixin, DeleteView):
    def get_success_url(self):
        return reverse('dataclips:list', kwargs={
            'organization': self.organization.slug})


class ClipPublicView(DetailView):
    model = Clip
    template_name = "dataclips/clip_public.html"
