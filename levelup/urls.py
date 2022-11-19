from django.contrib import admin
from django.urls import path
from levelupapi.views import register_user, check_user, GameTypeView
from django.conf.urls import include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
