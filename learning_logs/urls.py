"""Defines URL patterns for topics and entries"""
from django.urls import path
from learning_logs import views

app_name = 'learning_logs' #namespace for the app

urlpatterns= [
    path('', views.index, name='index' ),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Page that shows details for a topic
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # Page to add new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path ('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Delete a topic
    path("topics/delete/<int:topic_id>/", views.delete_topic, name="delete_topic"),
    # Delete entry
    path("entries/delete/<int:entry_id>/", views.delete_entry, name="delete_entry"),
]