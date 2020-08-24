import hgtk

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from topic.models import Brand
from topic.serializers import BrandSerializer
from django.db.models import Q


def get_brand_name(number):
    '''
    return a brand if number is given (not brand name)
    '''
    best_seller = {
            "0": "Chanel",
            "1": "Gucci",
            "2": "LOUIS VUITTON",
            "3": "Balenciaga",
            "4": "Prada",
            "5": "Hermès",
            "6": "Valentino",
            "7": "Cartier",
            "8": "Tiffany & Co",
    }
    brand_name = best_seller[number]
    return brand_name


class BrandSearch(APIView):
    '''Return Topic objects for list'''
    def get(self, request):
        brand_name = request.query_params['brand_name']
        if brand_name.isnumeric():
            brand_name = get_brand_name(brand_name)

        if brand_name.isspace():
            queryset = Brand.objects.all()
        else:
            criterion_1 = Q(eng_name__icontains=brand_name)
            criterion_2 = Q(kor_letters__contains=brand_name)
            queryset = Brand.objects.filter(
                criterion_1 | criterion_2).defer('kor_name')

        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update, delete the topic'''
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
