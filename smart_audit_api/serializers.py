# smart_audit_api/serializers.py
from rest_framework import serializers
from .models import AuditModel
from .models import TextModel


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextModel
        fields = '__all__'

class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditModel
        fields = '__all__'
