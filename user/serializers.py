from rest_framework import serializers
from rest_framework import views
from rest_framework.response import Response


class AddressSerializer(serializers.Serializer):
    '''Serialize address'''
    road_address = serializers.CharField(max_length=255)
    jibun_address = serializers.CharField(max_length=255)
    address_type = serializers.CharField(max_length=255)
    total_number = serializers.IntegerField()

    class Meta:
        fields = '__all__'
        read_only_fields = '__all__'
