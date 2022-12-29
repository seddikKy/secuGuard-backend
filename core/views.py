from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from core.form import PlanningForm
from .models import (Employee, Enterprise,Planning, Site, Tag, Zone)
from .cb_views import SCreateView, SDeleteView, SDetailView, SListView, STemplateView, SUpdateView

from django.shortcuts import render

# Auth views
class AppLoginView(LoginView):
    template_name = 'auth/login.html' 
    success_url = reverse_lazy('home')
    redirect_authenticated_user = reverse_lazy('home')


class AppLogoutView(LogoutView):
    template_name = 'auth/logout.html'


# Home view

class Home(STemplateView):
    template_name = 'home.html'
    login_url = reverse_lazy('login')


# Enterprise views

class EnterpriseListView(SListView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_enterprise',)


class EnterpriseDetailView(SDetailView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_enterprise',)
   

class EnterpriseCreateView(SCreateView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.add_enterprise',)
    fields = '__all__'
    success_url = reverse_lazy('enterprise_list')


class EnterpriseUpdateView(SUpdateView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_enterprise',)
    fields = '__all__'
    success_url = reverse_lazy('enterprise_list')


class EnterpriseDeleteView(SDeleteView):
    model = Enterprise
    template_name = "core/enterprise/enterprise_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_enterprise',)
    success_url = reverse_lazy('enterprise_list')


# Site views

class SiteListView(SListView):
    model = Site
    template_name = "core/site/site_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_site',)


class SiteDetailView(SDetailView):
    model = Site
    template_name = "core/site/site_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_site',)
    

class SiteCreateView(SCreateView):
    model = Site
    template_name = "core/site/site_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_site',)
    fields = '__all__'
    success_url = reverse_lazy('site_list')


class SiteUpdateView(SUpdateView):
    model = Site
    template_name = "core/site/site_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_site',)
    fields = '__all__'
    success_url = reverse_lazy('site_list')


class SiteDeleteView(SDeleteView):
    model = Site
    template_name = "core/site/site_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_site',)
    success_url = reverse_lazy('site_list')


# Zone views

class ZoneListView(SListView):
    model = Zone
    template_name = "core/zone/zone_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_zone',)


class ZoneDetailView(SDetailView):
    model = Zone
    template_name = "core/zone/zone_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_zone',)
    

class ZoneCreateView(SCreateView):
    model = Zone
    template_name = "core/zone/zone_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_zone',)
    fields = '__all__'
    success_url = reverse_lazy('zone_list')


class ZoneUpdateView(SUpdateView):
    model = Zone
    template_name = "core/zone/zone_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_zone',)
    fields = '__all__'
    success_url = reverse_lazy('zone_list')


class ZoneDeleteView(SDeleteView):
    model = Zone
    template_name = "core/zone/zone_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_zone',)
    success_url = reverse_lazy('zone_list')


# Employee views

class EmployeeListView(SListView):
    model = Employee
    template_name = "core/employee/employee_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_employee',)


class EmployeeDetailView(SDetailView):
    model = Employee
    template_name = "core/employee/employee_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_employee',)
    

class EmployeeCreateView(SCreateView):
    model = Employee
    template_name = "core/employee/employee_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_employee',)
    fields = '__all__'
    success_url = reverse_lazy('employee_list')


class EmployeeUpdateView(SUpdateView):
    model = Employee
    template_name = "core/employee/employee_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_employee',)
    fields = '__all__'
    success_url = reverse_lazy('employee_list')


class EmployeeDeleteView(SDeleteView):
    model = Employee
    template_name = "core/employee/employee_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_employee',)
    success_url = reverse_lazy('employee_list')


# tag views

class TagListView(SListView):
    model = Tag
    template_name = "core/tag/tag_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_tag',)


class TagDetailView(SDetailView):
    model = Tag
    template_name = "core/tag/tag_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_tag',)
    

class TagCreateView(SCreateView):
    model = Tag
    template_name = "core/tag/tag_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_tag',)
    fields = '__all__'
    success_url = reverse_lazy('tag_list')


class TagUpdateView(SUpdateView):
    model = Tag
    template_name = "core/tag/tag_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_tag',)
    fields = '__all__'
    success_url = reverse_lazy('tag_list')


class TagDeleteView(SDeleteView):
    model = Tag
    template_name = "core/tag/tag_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_tag',)
    success_url = reverse_lazy('tag_list')

# planning views

class PlanningListView(SListView):
    model = Planning
    template_name = "core/planning/planning_list.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_planning',)

    
    def get_context_data(self, *args, **kwargs):
        tag_number = Tag.objects.filter(zone_id=self.kwargs['zone']).count()
        context = super(PlanningListView, self).get_context_data()
        context["zone_id"] = self.kwargs['zone']
        context["selected_day"] = self.kwargs['selected_day_index']
        context["tag_number"] = tag_number
        return context

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(zone=self.kwargs['zone'],selected_day_index=self.kwargs['selected_day_index'])


class PlanningDetailView(SDetailView):
    model = Planning
    template_name = "core/planning/planning_detail.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.view_planning',)

    
class PlanningCreateView(SCreateView):
    model = Planning
    template_name = "core/planning/planning_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_planning',)
    #fields = '__all__'  
    #success_url = reverse_lazy('planning_list_filtred')
    form_class = PlanningForm

    
    def get_initial(self):
        return {'zone': self.kwargs['zone'], 'selected_day_index': self.kwargs['selected_day_index']}


    def form_valid(self, form):
        zone = Zone.objects.get(pk=self.kwargs['zone'])
        form.instance.zone = zone
        form.instance.selected_day_index = self.kwargs['selected_day_index']
        form.save()
     
        return super(PlanningCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('planning_list_filtred', kwargs={ 'zone': self.object.zone.pk, 'selected_day_index': self.object.selected_day_index})


class PlanningUpdateView(SUpdateView):
    model = Planning
    template_name = "core/planning/planning_form.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.change_planning',)
    fields = '__all__'
    #success_url = reverse_lazy('planning_list')

    def get_success_url(self):
        return reverse_lazy('planning_list_filtred', kwargs={ 'zone': self.object.zone.pk, 'selected_day_index': self.object.selected_day_index})



class PlanningDeleteView(SDeleteView):
    model = Planning
    template_name = "core/planning/planning_confirm_delete.html"
    login_url = reverse_lazy('login')
    permission_required = ('core.delete_planning',)
    #success_url = reverse_lazy('planning_list')

    def get_success_url(self):
        return reverse_lazy('planning_list_filtred', kwargs={ 'zone': self.object.zone.pk, 'selected_day_index': self.object.selected_day_index})
