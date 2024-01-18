from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.FAQ_list, name='faq_list'),
    path('faq/<int:pk>/', views.FAQ_Details, name='faq_detail'),
    path('terms-and-conditions/', views.TermsAndConditionsAPIView.as_view(), name='terms-and-conditions'),
    path('privacy-policy/', views.PrivacyPolicyAPIView.as_view(), name='privacy-policy'),
]