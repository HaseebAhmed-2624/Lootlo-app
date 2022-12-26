from django.urls import path, include
from api import views
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('signup/', views.UserModelViewSet.as_view({'post': 'create','get':'list'})),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('update/<int:pk>', views.UserModelViewSet.as_view({'put': 'update', 'patch': 'partial_update'})),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),

]
