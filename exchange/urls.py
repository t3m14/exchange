from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', include('user.urls')),
    path('exchange/', include('exchanging.urls')),
    path('withdraw/', include('withdraw.urls')),
]