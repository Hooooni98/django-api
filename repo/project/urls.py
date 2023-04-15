from django.urls import path, include
from django.http import JsonResponse

from rest_framework import routers

from project.admin import admin_site


def health_check(request):
    return JsonResponse({"status": "available"})


router_v1 = routers.SimpleRouter()

# register view set
# router_v1.register()

urlpatterns = [
    path("health_check/", health_check, name="health_check"),
    path("base_path", include(router_v1.urls)),
]

urlpatterns += [
    path("admin-path/", admin_site.urls),
]
