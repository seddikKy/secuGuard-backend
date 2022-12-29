from rest_framework import serializers

from core.models import (Employee, Enterprise, Site, Tag, PatrolLog, Planning, Zone)


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ['id', 'designation', 'created', 'modified']


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'designation','enterprise', 'created', 'modified']



class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id', 'designation','site', 'created', 'modified']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'designation','site', 'created', 'modified']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'zone','code_nfc', 'designation','order','observation', 'created', 'modified']


class PatrolLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatrolLog
        fields = ['id', 'tag','audio_path','image_path','description_anomaly','is_checked', 'created', 'modified']


class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = ['id', 'zone','selected_day_index','patrol_start_time','tolerated_time','observation', 'created', 'modified']
       