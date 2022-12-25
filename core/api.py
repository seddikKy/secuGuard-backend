from rest_framework import viewsets
from rest_framework import routers
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions

from core.models import (Employee, Enterprise, Site, TagHeader, TagDetail, Zone)
from core.serializers import (EmployeeSerializer, EnterpriseSerializer, SiteSerializer, 
    TagSerializer, TagDetailSerializer,ZoneSerializer)


class EnterpriseViewSet(viewsets.ReadOnlyModelViewSet):  # viewsets.ModelViewSet  --> Fill CRUD
    """
    A simple ViewSet for viewing object list and detail.
    .../core/api/enterprises       --> for list
    .../core/api/enterprises/2     --> For detail of enterprise 2

    """
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

    permission_classes = [IsAuthenticated, DjangoObjectPermissions]


class SiteViewSet(viewsets.ReadOnlyModelViewSet):  # viewsets.ModelViewSet  --> Fill CRUD
    """
    A simple ViewSet for viewing object list and detail.
    .../core/api/sites       --> for list
    .../core/api/sites/2     --> For detail of site 2

    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    permission_classes = [IsAuthenticated, DjangoObjectPermissions]


class ZoneViewSet(viewsets.ReadOnlyModelViewSet):  
    """
    A simple ViewSet for viewing object list and detail.
    .../core/api/zones       --> for list
    .../core/api/zones/2     --> For detail of zone 2

    """
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

    permission_classes = [IsAuthenticated, DjangoObjectPermissions]


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):  
    """
    A simple ViewSet for viewing object list and detail.
    .../core/api/employees       --> for list
    .../core/api/employees/2     --> For detail of employee 2

    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    permission_classes = [IsAuthenticated, DjangoObjectPermissions]


class TagViewSet(viewsets.ModelViewSet):  
    """
    A simple ViewSet for viewing object list and detail.
    .../core/api/tags       --> for list
    .../core/api/tags/2     --> For detail of tag 2

    """
    queryset = TagHeader.objects.all()
    serializer_class = TagSerializer

    permission_classes = [IsAuthenticated, DjangoObjectPermissions]


class TagDetailViewSet(viewsets.ModelViewSet):  
    """
    A simple ViewSet for viewing object list and detail.
    .../core/api/tag-details       --> for list
    .../core/api/tag-details/2     --> For detail of tagDetail 2

    """
    queryset = TagDetail.objects.all()
    serializer_class = TagDetailSerializer

    permission_classes = [IsAuthenticated, DjangoObjectPermissions]


# Registration
router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('enterprises', EnterpriseViewSet)
router.register('sites', SiteViewSet)
router.register('tags', TagViewSet)
router.register('tag-details', TagDetailViewSet)
router.register('zones', ZoneViewSet)