from django.shortcuts import render
from rest_framework import generics
from .models import Proxy
from .serializers import ProxySerializer


class ProxyListView(generics.ListAPIView):
    queryset = Proxy.objects.all()
    serializer_class = ProxySerializer


class ProxyDetailView(generics.RetrieveAPIView):
    queryset = Proxy.objects.all()
    serializer_class = ProxySerializer
    lookup_field = 'pk'
