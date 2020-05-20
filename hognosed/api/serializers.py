from rest_framework import serializers
from . import models

class ScenarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		fields = ('name', 'overlays',)
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


