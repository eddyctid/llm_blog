from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from rest_framework.authtoken.views import obtain_auth_token   # <-- add this
from apis.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('apis/token/', obtain_auth_token, name='api_token_auth'),  # <-- add this line
    path('apis/logout/', LogoutView.as_view(), name='api_logout'),

    # Swagger schema + UI
    path('apis/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('apis/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('apis/', include('apis.urls')),
]
