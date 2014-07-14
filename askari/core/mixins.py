from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..dataclips.models import Clip
from ..databases.models import Database


class LoginRequiredViewMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredViewMixin, self).dispatch(*args, **kwargs)


class GenericTemplateDataMixin(LoginRequiredViewMixin):
    def get_context_data(self, **kwargs):
        c = super(GenericTemplateDataMixin, self).get_context_data(**kwargs)
        clips = Clip.objects.filter(database__user__pk=self.request.user.pk)
        databases = Database.objects.filter(user__pk=self.request.user.pk)

        generic_data = {
            'total_clips': clips.count(),
            'total_bases': databases.count()
        }

        c.update(generic_data)
        return c
