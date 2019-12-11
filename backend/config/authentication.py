from rest_framework import authentication


class CsrfExemptSessionAuth(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return
