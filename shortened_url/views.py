from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import exceptions
from django.core.validators import URLValidator
from django.shortcuts import get_object_or_404
from .models import Url
from .validations import validate

class TargetUrlAPIView(APIView):
    def get(self, request, target_url):
        """
        대상 url과 함께 요청 시 단축 url을 반환
        """
        url_validator = URLValidator() 
        url_validator(target_url)

        try:
            entry = Url.objects.get(origin_url=target_url)
        except exceptions.ObjectDoesNotExist:
            entry = Url.create(target_url)

        return Response(request.META['HTTP_HOST'] + '/' + entry.shortened_url, status=201)


class ShortUrlAPIView(APIView):
    """
    단축 url과 함께 요청 시 해당 단축 url 접속 횟수 반환
    """
    def get(self, request, short_url):
        http_host = request.META['HTTP_HOST']
        index = short_url.find(http_host)
        slice_short_url = short_url[index + len(http_host) + 1:]
        entry = get_object_or_404(Url, shortened_url=slice_short_url)
        
        return Response(entry.count, status=200)


    """
    단축 url과 함께 요청 시 지정 단축 url을 삭제
    """
    def delete(self, request, short_url):
        http_host = request.META['HTTP_HOST']
        index = short_url.find(http_host)
        slice_short_url = short_url[index + len(http_host) + 1:]
        entry = get_object_or_404(Url, shortened_url=slice_short_url)
        entry.delete()
        return Response(status=204)



class RedirectUrlAPIView(APIView):
    def get(self, request):
        pass
