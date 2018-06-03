from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.core import exceptions
from django.core.validators import URLValidator
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from .models import Url
from .validations import validate

class TargetUrlAPIView(APIView):
    def get(self, request):
        """
        대상 url과 함께 요청 시 단축 url을 반환
        """
        url_validator = URLValidator() 
        target_url = request.GET.get('url', '')

        try:
            url_validator(target_url)
        except exceptions.ValidationError:
            raise serializers.ValidationError

        try:
            entry = Url.objects.get(origin_url=target_url)
        except exceptions.ObjectDoesNotExist:
            entry = Url.create(target_url)


        return Response(settings.DOMAIN + entry.shortened_url, status=201)


class ShortUrlAPIView(APIView):
    """
    단축 url과 함께 요청 시 해당 단축 url 접속 횟수 반환
    """
    def get(self, request):
        short_url = request.GET.get('url', '')
        http_host = settings.DOMAIN
        index = short_url.find(http_host)
        slice_short_url = short_url[index + len(http_host):]
        entry = get_object_or_404(Url, shortened_url=slice_short_url)
        
        return Response(entry.count, status=200)


    """
    단축 url과 함께 요청 시 지정 단축 url을 삭제
    """
    def delete(self, request, short_url):
        http_host = settings.DOMAIN
        index = short_url.find(http_host)
        slice_short_url = short_url[index + len(http_host):]
        entry = get_object_or_404(Url, shortened_url=slice_short_url)
        entry.delete()
        return Response(status=204)



class RedirectUrlAPIView(APIView):
    """
    단축 url 접속 시 원래 url로 Redirect (접속 횟수 카운트)
    """
    def get(self, request, redirect_url):
        entry = get_object_or_404(Url, shortened_url=redirect_url)
        entry.count += 1
        entry.save()
        return redirect(entry.origin_url)




