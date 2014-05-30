from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredViewMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
       return super(LoginRequiredViewMixin, self).dispatch(*args, **kwargs)
