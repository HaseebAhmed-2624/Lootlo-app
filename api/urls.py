from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenRefreshView
from api.auth import CustomTokenObtainPairView

urlpatterns = [
    path('signup/', views.UserModelViewSet.as_view({'post': 'create'}), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),

    path('list/', views.UserModelViewSet.as_view({'get': 'list'}), name='list'),
    path('retrieve/', views.UserModelViewSet.as_view({'get': 'retrieve'})),
    path('update/', views.UserModelViewSet.as_view({'put': 'update', 'patch': 'partial_update'})),
    path('delete/', views.UserModelViewSet.as_view({'delete': 'destroy'})),
    path('verifytoken/', views.VerifyToken.as_view(), name='verifytoken')
]
