import requests

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import User, Profile
from info_share.my_settings import ADDRESS_KEY


JUSO_OPEN_API = "http://www.juso.go.kr/addrlink/addrLinkApi.do"
PAGE_PER_DATA = 10


def call_juso_api(address, address_type, page, start, end):
    '''
    1. Description: Return addresses(json type)
    2. 관련 링크: http://www.juso.go.kr/    '''

    res = requests.get(
        JUSO_OPEN_API,
        params={
            'currentPage': 1,
            'countPerPage': 200,
            'resultType': 'json',
            'confmKey': ADDRESS_KEY['confmKey'],
            'keyword': address,
        },
    )
    raw_addresses = res.json()
    parsed_addresses = raw_addresses["results"]["juso"]

    address_result = [
        {
            "road_address": address["roadAddrPart1"],
            "jibun_address": address["jibunAddr"],
        }
        for address in parsed_addresses
            if "서울" in address["jibunAddr"]
    ]
    total_number = len(address_result)

    address_info = {}
    address_info["total_number"] = total_number
    address_info["address_type"] = address_type
    address_info["address_result"] = address_result[start:end]

    return address_info


def get_url_params(request, start=0, end=PAGE_PER_DATA):
    '''
    - helper function -
    Return url parameters (key: 'address', 'page')
    '''

    address = request.GET.getlist('address', [''])
    address = address[0]
    if '동' in address:
        address_type = 'jibun'
    else:
        address_type = 'road'

    page = request.GET.getlist('page', 1)
    if int(page[0]) > 0:
        page = int(page[0])
        start = PAGE_PER_DATA * (page - 1)
        end   = PAGE_PER_DATA * page

    return address, address_type, page, start, end


class HelloView(APIView):
    '''Test the REST API'''
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, world'}
        return Response(content)


class AddressSearch(APIView):
    '''Return address results based on user_input'''
    def get(self, request):
        address, address_type, page, \
        start, end = get_url_params(request)
        try:
            address_info = call_juso_api(address, address_type, page, start, end)
            return Response(address_info, status=status.HTTP_200_OK)

        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
