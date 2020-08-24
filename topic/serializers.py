from rest_framework import serializers
from topic.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    '''Topic serializer'''
    class Meta:
        model = Brand
        fields = ('kor_name', 'eng_name',)
