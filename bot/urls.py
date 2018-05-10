from django.contrib import admin
from django.conf.urls import url
from meal import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^keyboard/', views.keyboard )
]
