from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginView, LogoutView, CheckLogin
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('checklogin/', CheckLogin.as_view(), name='checklogin'),
		path('logout/', LogoutView.as_view(), name='logout'),

    path('inventory/', include('inventory.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
