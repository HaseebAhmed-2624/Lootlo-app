from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenRefreshView
from api.auth import CustomTokenObtainPairView
urlpatterns = [
    path('list/', views.UserModelViewSet.as_view({'get': 'list'}), name='list'),
    path('retrieve/<int:pk>', views.UserModelViewSet.as_view({'get': 'retrieve'})),
    path('signup/', views.UserModelViewSet.as_view({'post': 'create'}), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('update/<int:pk>', views.UserModelViewSet.as_view({'put': 'update', 'patch': 'partial_update'})),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    # path('usertypes/',views.ListUserTypes.as_view(),name='users')
]
