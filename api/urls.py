from django.urls import path
from .views import health_check, profile_api, admin_api

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('profile/', profile_api, name='profile_api'),
    path('admin/', admin_api, name='admin_api')
]