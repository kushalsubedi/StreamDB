from django.urls import path
from .views import (
    login_user,
    Registerview,
    VerifyOTPView,
    ForgetPasswordView,
    ResetPasswordView,
 
)

urlpatterns = [
  
    path('login/', login_user, name='login_user'),
    path ('register/',Registerview.as_view(),name='register'),
    path ('verify/',VerifyOTPView.as_view(),name='verify'),
    path ('forgotpassword/',ForgetPasswordView.as_view(),name='forgotpassword'),
    path ('resetpassword/',ResetPasswordView.as_view(),name='resetpassword'),
]
