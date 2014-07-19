from django.db import models
from django.db.models.query import QuerySet


class ClipScopesMixin(object):
    def by_user(self, user):
        return self.filter(database__user=user)


class ClipScopesQuerySet(QuerySet, ClipScopesMixin):
    pass


class ClipScopeManager(models.Manager, ClipScopesMixin):
    def get_query_set(self):
        return ClipScopesQuerySet(self.model, using=self._db)
