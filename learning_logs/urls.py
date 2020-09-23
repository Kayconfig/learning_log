from django.urls import path
from learning_logs import views

app_name = 'learning_logs' #namespace for the app

urlpatterns= [
    path('', views.index, name='index' ),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Page that shows details for a topic
    path('topics/<int:topic_id>', views.topic, name='topic'),
]