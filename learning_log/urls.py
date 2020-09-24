from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')), #base app for this django project
    path('users/', include('users.urls')),
    
]
