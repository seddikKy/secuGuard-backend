from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, TemplateView


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

class STemplateView(LoginRequiredMixin,TemplateView):
    pass
