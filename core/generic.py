from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, TemplateView
from django.views.generic.base import ContextMixin

from django.db import models


class SListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    pass


class SDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    pass


class SCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    pass


class SUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    pass


class SDeleteView(DeleteView):
    pass


class STemplateView(TemplateView):
    pass


class ParentObjectMixin(ContextMixin):
    """
    Provide the ability to retrieve a single object for further manipulation.
    """
    parent_model = None
    parent_pk_url_kwarg = 'parent_pk'

    def get_parent_object(self, queryset=None):
        """
        Return the object the view is displaying.

        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.parent_model._default_manager.all()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.parent_pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        # If none of those are defined, it's an error.
        if pk is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    def get_parent_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {'parent_object': self.get_parent_object()}
        context.update(kwargs)
        return super().get_context_data(**context)


class SParentDetailChildListView(ParentObjectMixin, SListView):
    """
    Master detail generic view
    """
    parent_field = 'parent'  # Child foreign key for parent model

    def get_queryset(self):
        return super().get_queryset().filter(**{self.parent_field: self.get_parent_object()})

    def get_context_data(self, *arg, **kwargs):
        context = super().get_context_data(*arg, **kwargs)
        context.update(self.get_parent_context_data())
        return context


class SParentDetailChildCreateView(ParentObjectMixin, SCreateView):
    """
    Master detail generic view
    """
    parent_field = 'parent'  # Child foreign key for parent model

    def get_queryset(self):
        return super().get_queryset().filter(**{self.parent_field: self.get_parent_object()})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_parent_context_data())
        return context


class SParentDetailChildUpdateView(ParentObjectMixin, SUpdateView):
    """
    Master detail generic view
    """
    parent_field = 'parent'  # Child foreign key for parent model

    def get_queryset(self):
        return super().get_queryset().filter(**{self.parent_field: self.get_parent_object()})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_parent_context_data())
        return context


class SParentDetailChildDeleteView(ParentObjectMixin, SDeleteView):
    """
    Master detail generic view
    """
    parent_field = 'parent'  # Child foreign key for parent model

    def get_queryset(self):
        return super().get_queryset().filter(**{self.parent_field: self.get_parent_object()})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_parent_context_data())
        return context


class SParentDetailChildDetailView(ParentObjectMixin, SDetailView):
    """
    Master detail generic view
    """
    parent_field = 'parent'  # Child foreign key for parent model

    def get_queryset(self):
        return super().get_queryset().filter(**{self.parent_field: self.get_parent_object()})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_parent_context_data())
        return context

