from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from core.views import AcessoriosViewSet, CorViewSet, ModeloViewSet, UserRegistrationView, UserViewSet
from core.views.veiculo import VeiculoViewSet

router = DefaultRouter()
router.register(r'acessorios', AcessoriosViewSet, basename='acessorios')
router.register(r'cores', CorViewSet, basename='cores')
router.register(r'modelo', ModeloViewSet, basename='modelo')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'veiculos', VeiculoViewSet, basename='veiculos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/registro/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/', include(router.urls)),
]