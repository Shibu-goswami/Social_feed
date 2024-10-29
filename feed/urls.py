from django.urls import path
from . import views
from .views import  logout_view 

app_name = 'feed'


urlpatterns = [
    path('', views.feed, name='feed'),
    path('post_message/', views.post_message, name='post_message'),
    path('post_comment/<int:message_id>/', views.post_comment, name='post_comment'),
    path('like_message/<int:message_id>/', views.like_message, name='like_message'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('add_message/', views.add_message, name='add_message'),
    path('logout/', logout_view, name='logout'),
    
]
