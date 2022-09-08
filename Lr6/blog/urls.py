from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', views.BlogCreateView.as_view(), name='new_blog'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
]




