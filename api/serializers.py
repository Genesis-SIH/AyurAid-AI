from rest_framework import serializers

class YourSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=255)
