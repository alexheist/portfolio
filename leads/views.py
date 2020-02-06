import requests

from django.conf import settings

from . import models


#    def create(self, request, *args, **kwargs):
#        token = request.data.pop("recaptchaToken")
#        if token:
#            data = {"secret": settings.RECAPTCHA_SECRET, "response": token}
#            r = requests.post(
#                "https://www.google.com/recaptcha/api/siteverify", data=data
#            )
#            result = r.json()
#        if result["success"] == True and result["score"] >= 0.5:
#            serializer = self.get_serializer(data=request.data)
#            serializer.is_valid(raise_exception=True)
#            self.perform_create(serializer)
#            headers = self.get_success_headers(serializer.data)
#            return Response(status.HTTP_201_CREATED, headers=headers)
#        return Response(status.HTTP_200_OK,)
