from django.urls import path
from . import views

urlpatterns = [
    path('', views.poem, name='poem'),  # Maps to the poem list view
    path('<int:pk>/', views.poem_detail, name='poem_detail'),  # Maps to the poem detail view
]
