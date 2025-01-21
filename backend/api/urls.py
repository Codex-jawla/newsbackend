from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from backend import settings
from .views import *

router = routers.DefaultRouter()
router.register(r'category',CategoryView )
router.register(r'news',NewsView )

urlpatterns = [
    path('',include(router.urls) ),
]

