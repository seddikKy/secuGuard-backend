from rest_framework import serializers

from core.models import (Employee, Enterprise, Site, TagHeader, TagDetail, Zone)


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ['id', 'designation', 'created', 'modified']


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'designation','id_enterprise', 'created', 'modified']



class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id', 'designation','id_site', 'created', 'modified']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'designation','id_site', 'created', 'modified']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagHeader
        fields = ['id', 'id_zone','code_nfc', 'designation','order','observation', 'created', 'modified']


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagDetail
        fields = ['id', 'id_tag','memo_path','image_path','description_anomaly','is_checked', 'created', 'modified']