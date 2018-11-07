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
    r'notebook',
    cuaderno_views.NotebookModelViewSet
)
#   Usuario
router.register(
    r'user',
    cuaderno_views.UserModelViewSet
)
#   Nota
router.register(
    r'note',
    notas_views.NoteModelViewSet
)
#   Amistad
router.register(
    r'friendship',
    notas_views.FriendshipModelViewSet
)
#   Compartido
router.register(
    r'shared',
    notas_views.SharedModelViewSet
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth-jwt/', obtain_jwt_token),
    path('api/v1/auth-jwt-refresh/', refresh_jwt_token),
    path('api/v1/auth-jwt-verify/', verify_jwt_token),
    path('api/v1/', include(router.urls))
]