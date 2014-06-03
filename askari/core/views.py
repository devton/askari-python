from django.views.generic import TemplateView
from .mixins import GenericTemplateDataMixin


class DashboardView(GenericTemplateDataMixin, TemplateView):
    template_name = 'core/dashboard.html'