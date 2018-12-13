from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .models import Compress
from django_downloadview import ObjectDownloadView
app_name='compress'

urlpatterns=[

            path('',views.image_upload_view,name='upload'),
            # path('result/',views.result,name='result'),
            path('compress_image/',views.compress_image,name='image_compress'),
            path('download/',views.ImageDownloadView.as_view(),name='download'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
