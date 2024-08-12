from django.urls import path
from . import views

# Here is your interview app's URLs
urlpatterns = [
    path('', views.interview, name='interview'),  # Maps to the interview list view
    path('<int:pk>/', views.interview_detail, name='interview_detail'),  # Corrected this line
]
