from django.urls import path
from . import views

# Here is your app's urls
urlpatterns=[
    path('',views.index, name='index'),
    path('aboutus',views.about, name='aboutus'),
    path('product_detail/<pk>',views.blog_detail,name='details'),
] 