import blog.views
import leads.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = []
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)