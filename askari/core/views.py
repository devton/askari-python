from django.views.generic import TemplateView, CreateView, RedirectView
from django.core.urlresolvers import reverse
from .mixins import GenericTemplateDataMixin
from .forms import UserRegistrationForm


class DashboardView(GenericTemplateDataMixin, TemplateView):
    template_name = 'core/dashboard.html'


class UserLoginView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        org = self.request.user.userprofile.organizations.first()
        return reverse('dashboard', kwargs={'organization': org.slug})


class UserRegistrationView(CreateView):
    template_name = 'core/registration.html'
    form_class = UserRegistrationForm

    def get_success_url(self):
        return reverse('dashboard', self.organization.slug)
