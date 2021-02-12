from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('api/predict', views.KospiPredictAPIView.as_view(), name='predict_kospi_api'),
    path('chart', views.ChartView.as_view(), name='chart'),
]

