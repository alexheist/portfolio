from rest_framework import viewsets, permissions
from . import models, serializers

class IsPostOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_authenticated

class LeadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows leads to be viewed or edited
    """
    permission_classes = [IsPostOrIsAuthenticated]
    queryset = models.Lead.objects.all().order_by('-timestamp')
    serializer_class = serializers.LeadSerializer
