from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /service/5/
    path('<int:vehicle_id>/', views.detail, name='detail'),
]
