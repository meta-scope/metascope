from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("metascope_app/", include("metascope_app.urls")),
    path("admin/", admin.site.urls),
]