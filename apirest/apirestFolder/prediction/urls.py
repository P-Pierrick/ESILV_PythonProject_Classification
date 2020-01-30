from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.Human_Activity_Model_Predict.as_view(), name='predict')
]
