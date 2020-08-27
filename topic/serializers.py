from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from topic.models import Brand, SellCategory


class BrandSerializer(serializers.ModelSerializer):
    '''Brand serializer'''

    class Meta:
        model = Brand
        fields = ('kor_name', 'eng_name',)


class SellCategorySerializer(serializers.ModelSerializer):
    '''Category serializer for Brand'''

    class Meta:
        model = SellCategory
        fields = ('name',)

