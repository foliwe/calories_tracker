from django.urls import path
from .views import index, delete_consume


urlpatterns = [
    path('', index, name='tracker'),
    path('delete/<int:pk>/', delete_consume, name='delete'),

]
