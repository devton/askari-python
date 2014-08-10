from django.db import models
from django.db.models.query import QuerySet


class ClipScopesMixin(object):
    def by_user(self, user):
        return self.filter(database__user=user)

    def by_organization(self, organization):
        params = {
            'database__user__userprofile__' + 
            'organizations__slug': organization
        }
        return self.filter(**params)


class ClipScopesQuerySet(QuerySet, ClipScopesMixin):
    pass


class ClipScopeManager(models.Manager, ClipScopesMixin):
    def get_query_set(self):
        return ClipScopesQuerySet(self.model, using=self._db)
