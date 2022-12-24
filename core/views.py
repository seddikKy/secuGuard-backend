from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, TemplateView
from .models import (Employee, Enterprise, Site, TagHeader, Zone)


# Auth views
class AppLoginView(LoginView):
    template_name = 'auth/login.html' 
    success_url = reverse_lazy('home')
    redirect_authenticated_user = reverse_lazy('home')


class AppLogoutView(LogoutView):
    template_name = 'auth/logout.html'


# Home view

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = reverse_lazy('login')


# Enterprise views

class EnterpriseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_enterprise',)


class EnterpriseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_enterprise',)
   

class EnterpriseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.add_enterprise',)
    fields = '__all__'
    success_url = reverse_lazy('enterprise_list')


class EnterpriseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_enterprise',)
    fields = '__all__'
    success_url = reverse_lazy('enterprise_list')


class EnterpriseDeleteView(DeleteView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_enterprise',)
    success_url = reverse_lazy('enterprise_list')


# Site views

class SiteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Site
    template_name = "core/site/site_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_site',)


class SiteDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Site
    template_name = "core/site/site_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_site',)
    

class SiteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Site
    template_name = "core/site/site_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_site',)
    fields = '__all__'
    success_url = reverse_lazy('site_list')


class SiteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Site
    template_name = "core/site/site_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_site',)
    fields = '__all__'
    success_url = reverse_lazy('site_list')


class SiteDeleteView(DeleteView):
    model = Site
    template_name = "core/site/site_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_site',)
    success_url = reverse_lazy('site_list')


# Zone views

class ZoneListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Zone
    template_name = "core/zone/zone_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_zone',)


class ZoneDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Zone
    template_name = "core/zone/zone_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_zone',)
    

class ZoneCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Zone
    template_name = "core/zone/zone_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_zone',)
    fields = '__all__'
    success_url = reverse_lazy('zone_list')


class ZoneUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Zone
    template_name = "core/zone/zone_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_zone',)
    fields = '__all__'
    success_url = reverse_lazy('zone_list')


class ZoneDeleteView(DeleteView):
    model = Zone
    template_name = "core/zone/zone_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_zone',)
    success_url = reverse_lazy('zone_list')


# Employee views

class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Employee
    template_name = "core/employee/employee_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_employee',)


class EmployeeDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Employee
    template_name = "core/employee/employee_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_employee',)
    

class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Employee
    template_name = "core/employee/employee_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_employee',)
    fields = '__all__'
    success_url = reverse_lazy('employee_list')


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    template_name = "core/employee/employee_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_employee',)
    fields = '__all__'
    success_url = reverse_lazy('employee_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "core/employee/employee_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_employee',)
    success_url = reverse_lazy('employee_list')


    # tag views

class TagListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = TagHeader
    template_name = "core/tag/tag_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_tag',)


class TagDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = TagHeader
    template_name = "core/tag/tag_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_tag',)
    

class TagCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TagHeader
    template_name = "core/tag/tag_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_tag',)
    fields = '__all__'
    success_url = reverse_lazy('tag_list')


class TagUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TagHeader
    template_name = "core/tag/tag_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_tag',)
    fields = '__all__'
    success_url = reverse_lazy('tag_list')


class TagDeleteView(DeleteView):
    model = TagHeader
    template_name = "core/tag/tag_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_tag',)
    success_url = reverse_lazy('tag_list')