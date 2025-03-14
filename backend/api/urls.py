from django.urls import path # type: ignore
from django.conf.urls import include # type: ignore

router = DefaultRouter() # type: ignore

urlpatterns = [
    path('api/', include(router.urls)),
]