# serializers.py
from rest_framework import serializers

class YourSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=120)
    timestamp = serializers.DateTimeField()
    data = serializers.JSONField(allow_null=True)

