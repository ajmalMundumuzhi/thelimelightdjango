from django.urls import path
from . import views

urlpatterns = [
    path('/', views.article, name='article'),  
    path('<int:pk>/', views.article_detail, name='article_detail'),
]
