from django.urls import path, include
from .views import sign_up, lk

urlpatterns = [
    path('', lk, name='lk'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign_up/', sign_up, name="sign-up"),
]
