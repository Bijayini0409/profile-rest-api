from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializing a namefiled for testing our APIView"""
    name=serializers.CharField(max_length=10)
