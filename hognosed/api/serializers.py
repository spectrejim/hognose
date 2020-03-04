from rest_framework import serializers
from . import models

class ScenarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		fields = ('name', 'maps', 'overlays', 'sides', 'location', 'time', 'source', 'front',)
		model = models.Scenario

class ProductSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                fields = ('name', 'scenarios', 'maps', 'overlays', 'location', 'date', 'publisher',) 
                model = models.Product

class MapsSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                fields = ('name', 'description', 'source', 'publisher',) 
                model = models.Maps

class OverlaysSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                fields = ('name', 'description', 'source', 'publisher',)
                model = models.Overlays        


