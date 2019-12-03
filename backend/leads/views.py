import requests
from django.conf import settings
from rest_framework import (
    authentication,
    permissions,
    status,
    viewsets
)
from rest_framework.response import Response
from config import authentication as c_auth
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
    authentication_classes = (
        c_auth.CsrfExemptSessionAuth,
        authentication.BasicAuthentication
    )
    permission_classes = [IsPostOrIsAuthenticated]
    queryset = models.Lead.objects.all().order_by('-timestamp')
    serializer_class = serializers.LeadSerializer

    def create(self, request, *args, **kwargs):
        token = request.data.pop('recaptchaToken')
        if token:
            data = {
                'secret': settings.RECAPTCHA_SECRET,
                'response': token
            }
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data = data
            )
            result = r.json()
        if result['success'] == True and result['score'] >= 0.5:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                status.HTTP_201_CREATED,
                headers = headers
            )
        return Response(
            status.HTTP_200_OK,
        )
