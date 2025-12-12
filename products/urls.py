#from rest_framework import routers
#from .views import ProductViewSet

#router = routers.DefaultRouter()
#router.register(r'products', ProductViewSet)

#urlpatterns = router.urls

#________________------------------------------------------------------------------

# products/urls.py
# products/urls.py
from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView, CategoryListCreateAPIView, CategoryDetailAPIView
from .views_auth import login_view, register_view, logout_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),

    # Auth
    path('login/', login_view, name='api_login'),
    path('register/', register_view, name='api_register'),
    path('logout/', logout_view, name='api_logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
