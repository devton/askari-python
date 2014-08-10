from django.db import models
from django.db.models.query import QuerySet


class DatabaseScopesMixin(object):
    def by_organization(self, organization):
        return self.filter(organization__pk=organization.pk)


class DatabaseScopesQuerySet(QuerySet, DatabaseScopesMixin):
    pass


class DatabaseScopeManager(models.Manager, DatabaseScopesMixin):
    def get_query_set(self):
        return DatabaseScopesQuerySet(self.model, using=self._db)
