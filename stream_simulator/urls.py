from django.contrib import admin
from django.conf.urls import url
from reporter import views

urlpatterns = [
    url(r'^client/(?P<client_id>[^/]+)/?$', views.client_sampling, name='index'),
    url(r'admin/', admin.site.urls),
]
