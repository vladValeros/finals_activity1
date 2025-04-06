from django.urls import path
from .views import predict_sleep_disorder

urlpatterns = [
    path('predict/', predict_sleep_disorder, name='predict'),
]
