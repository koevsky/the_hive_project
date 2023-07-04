from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-admin/', include('custom_admin_app.urls')),
    path('accounts/', include('accounts_app.urls')),
    path('', include('hive_app.urls')),
]
