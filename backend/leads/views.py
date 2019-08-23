from rest_framework import (
    viewsets,
    permissions,
    status
)
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            status.HTTP_201_CREATED,
            headers = headers
        )
