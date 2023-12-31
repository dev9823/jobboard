from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
    path("api/", include("profiles.urls")),
    path("api/", include("job.urls")),
]

# urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
