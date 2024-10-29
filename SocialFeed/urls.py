from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Register and Login
    path('feed/', include('feed.urls')),          # Feed and message functionality
    path('logout/', LogoutView.as_view(), name='logout'),
]
