from django.contrib import admin
from django.conf.urls import url,include
from meal import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^keyboard/', views.keyboard )
]
