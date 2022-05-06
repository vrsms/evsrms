from django.urls import path
from . import views

app_name = 'suggestions'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /service/5/
    path('<int:suggestion_id>/', views.detail, name='detail'),
]
