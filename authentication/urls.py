
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    # Authentication Paths
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('sauth/',include('djoser.urls')),
    # path('sauth/',include('djoser.urls.jwt')),
    path('sauth/',include('djoser.social.urls')),
    path('sauth/',include('djoser.social.urls')),
]
