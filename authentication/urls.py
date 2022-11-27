from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserCreateView, Logout

urlpatterns = [
    path("create/", UserCreateView.as_view(), name='create_user'),
    path("login/", views.obtain_auth_token, name="login_user"),
    path("logout/", Logout.as_view(), name="logout_user"),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]