from django.urls import path
from learning_logs import views

app_name = 'learning_logs' #namespace for the app

urlpatterns= [
    path('', views.index, name='index' ),
]