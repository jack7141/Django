from django.conf.urls import url
from meal import views
urlpatterns = [
    url(r'^keyboard', views.keyboard),
    url(r'^message', views.message),	
]
