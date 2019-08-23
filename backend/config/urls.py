from django.urls import path, include
from rest_framework import routers
from leads import views

router = routers.DefaultRouter()
router.register(r'leads', views.LeadViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
