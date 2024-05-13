"""Defines URL patterns for learning_logs."""

from django.urls import path # path function needed to map URLs to views
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('',views.index,name='index'),

    # Page that shows all the topics
    path('topics/',views.topics,name='topics'),

    # Individual Topic page
    path('topics/<int:topic_id>/',views.topic,name='topic'),

    # New topic URL in the form
    path('new_topic/',views.new_topic,name='new_topic'),

    # New Entry URL in the form
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    
    # Edit Entry 
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry')

]