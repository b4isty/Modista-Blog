from rest_framework import serializers


class SearchResponseSerializer(serializers.Serializer):
    """
    Serializer for Search response which only
    needs title field
    """
    title = serializers.CharField()
