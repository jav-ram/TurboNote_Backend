"""TurboNote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from cuaderno import views as cuaderno_views 
from nota import views as notas_views

# Router creation
router = DefaultRouter()

# Client
#   Cuaderno
router.register(
    r'cuaderno',
    cuaderno_views.CuadernoModelViewSet
)
#   Usuario
router.register(
    r'usuario',
    cuaderno_views.UserModelViewSet
)
#   Nota
router.register(
    r'nota',
    notas_views.NotaModelViewSet
)
#   Amistad
router.register(
    r'amistad',
    notas_views.AmistadModelViewSet
)
#   Compartido
router.register(
    r'compartido',
    notas_views.CompartidoModelViewSet
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
    path('api/v1/', include(router.urls))
]