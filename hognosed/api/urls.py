from django.urls import include,path
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('Scenario', views.ScenarioViewSet)
router.register('Product', views.ProductViewSet)
router.register('Maps', views.MapsProductViews)
router.register('Overlays', views.OverlaysProductViews)
urlpatterns = router.urls
