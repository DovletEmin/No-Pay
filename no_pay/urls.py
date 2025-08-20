from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),

    #path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
   # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(), name="docs"),

    path('api/auth/', include("users.urls")),

    path('api/catalog/', include("catalog.urls")),
    
    path("api/cart/", include("cart.urls")),

    path("api/orders/", include("orders.urls"),),

    path("api/payments/", include("payments.urls")),
]
