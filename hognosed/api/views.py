from django.shortcuts import render

# Create your views here.

from rest_framework import generics, viewsets
from .models import Scenario,Product,Maps,Overlays
from .serializers import ScenarioSerializer,ProductSerializer,MapsSerializer,OverlaysSerializer

# Create your views here.
class ScenariolList(generics.ListCreateAPIView):
        queryset = Scenario.objects.all()
        serializer_class = ScenarioSerializer
class ScenarioDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Scenario.objects.all()
        serializer_class = ScenarioSerializer
class ScenarioViewSet(viewsets.ModelViewSet):
        queryset = Scenario.objects.all().order_by('name')
        serializer_class = ScenarioSerializer

class ProductlList(generics.ListCreateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all().order_by('name')
        serializer_class = ProductSerializer

class MapslList(generics.ListCreateAPIView):
        queryset = Maps.objects.all()
        serializer_class = MapsSerializer
class MapsDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Maps.objects.all()
        serializer_class = MapsSerializer
class MapsProductViews(viewsets.ModelViewSet):
        queryset = Maps.objects.all().order_by('name')
        serializer_class = MapsSerializer

class OverlayslList(generics.ListCreateAPIView):
        queryset = Overlays.objects.all()
        serializer_class = OverlaysSerializer
class OverlaysDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Overlays.objects.all()
        serializer_class = OverlaysSerializer
class OverlaysProductViews(viewsets.ModelViewSet):
        queryset = Overlays.objects.all().order_by('name')
        serializer_class = OverlaysSerializer
