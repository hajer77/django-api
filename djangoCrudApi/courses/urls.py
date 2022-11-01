from django.urls import re_path as url
from courses import views

from django.conf.urls.static import static 
from django.conf import settings


urlpatterns=[
    url(r'^coursesapi$',views.courseApi),
    url(r'^coursesapi/([0-9]+)$',views.courseApi),

    url(r'^coursesapi/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
