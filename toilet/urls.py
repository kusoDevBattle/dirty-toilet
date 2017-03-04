from django.conf.urls import url
from toilet import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^toilet$', views.toilets, name='toilets'),
    url(r'^register$', views.register, name='register'),
]
