import django_filters
from .models import Clip


class ClipFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Clip
        fields = ['name']
