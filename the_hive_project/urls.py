from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-admin/', include('custom_admin_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('bee-garden/', include('apiary_app.urls')),
    path('product/', include('product_app.urls')),
    path('cart/', include('cart_app.urls')),
    path('', include('hive_app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


