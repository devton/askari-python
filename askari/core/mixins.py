from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..dataclips.models import Clip
from ..databases.models import Database


class LoginRequiredViewMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredViewMixin, self).dispatch(*args, **kwargs)


class GenericTemplateDataMixin(object):
    def get_context_data(self, **kwargs):
        context = super(GenericTemplateDataMixin, self).get_context_data(**kwargs)

        generic_data = {
            'total_clips': Clip.objects.filter(database__user__pk=self.request.user.pk).count(),
            'total_bases': Database.objects.filter(user__pk=self.request.user.pk).count()
        }

        context.update(generic_data)
        return context
