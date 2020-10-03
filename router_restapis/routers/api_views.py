from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets , status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny
from routers.serializers import RouterSerializer
from routers.models import Router


class RouterCreateAPIView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RouterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class RouterUpdateAPIView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        ip = request.GET.get('ip')
        obj = Router.objects.get(ip = ip)
        serializer = RouterSerializer(obj)
        return Response(serializer.data)


    def post(self, request):
        ip = request.data.get('ip')
        obj = Router.objects.get(ip = ip)
        obj.__dict__.update(request.data)
        obj.save()
        return Response({'message' : 'update successfully'})


class RouterListBasedonTypeAPIView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        type = request.GET.get('type')
        objs = Router.objects.filter(type = type)
        serializer = RouterSerializer(objs, many=True)
        return Response(serializer.data)
        

class RouterListBasedonIPrangeAPIView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        start_ip = request.GET.get('start_ip')
        end_ip = request.GET.get('end_ip')
        objs = Router.objects.filter(ip__range=[start_ip, end_ip])
        serializer = RouterSerializer(objs, many=True)
        return Response(serializer.data)
       

class DeleteRouterAPIView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ip = request.data.get('ip')
        obj = Router.objects.get(ip = ip)
        obj.delete()
        return Response({'message' : 'Delete successfully'})