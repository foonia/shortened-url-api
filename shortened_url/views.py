from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import exceptions
from django.core.validators import URLValidator
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
    def get(self, request):
        pass
    
    def delete(self, request):
        pass


class RedirectUrlAPIView(APIView):
    def get(self, request):
        pass
