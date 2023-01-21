from datetime import datetime
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
        fields = ['id', 'designation','code_pin','site', 'created', 'modified']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'zone','code_nfc', 'designation','order','observation', 'created', 'modified']



class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = '__all__'
       

class PatrolLogSerializer(serializers.ModelSerializer):
    zone_id = serializers.IntegerField(source='tag.zone.id', read_only=True)
    zone_name = serializers.CharField(source='tag.zone.designation', read_only=True)
    tag_name = serializers.CharField(source='tag.designation', read_only=True)
    selected_day_index = serializers.IntegerField(source='planning.selected_day_index', read_only=True)
    tag_order = serializers.IntegerField(source='tag.order', read_only=True)
    now = serializers.SerializerMethodField()
    
    class Meta:
        model = PatrolLog
        fields = ['id','planning','check_datetime','check_tolerance','selected_day_index','tag','tag_name'
        ,'tag_order','zone_id','zone_name','audio_path','image_path','description_anomaly','is_checked',
         'created', 'modified', 'now']

    def get_now(self, obj):
        return datetime.now()
