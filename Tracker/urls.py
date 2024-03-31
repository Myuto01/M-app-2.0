from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.homepage, name='home'),
  path('add-habits/', views.add_habits, name='add-habits'),
  path('habit-list/', views.habit_list, name='habit-list'),
  path('notepad/', views.notepad, name='notepad'),
  path('note-details/<int:note_id>/', views.note_detail, name='note-detail'),
  path('note-details/<int:note_id>/edit/', views.edit_notepad, name='edit-notepad'),
  path('notes/', views.notes, name='notes'),
  path('delete-notes/<int:note_id>/', views.delete_note, name='delete-notes'),
  path('goals/', views.goal_list, name='goal-list'),
  path('goals/<int:goal_id>/', views.goal_detail, name='goal-detail'),
  path('edit-goal/<int:goal_id>/', views.edit_goal, name='edit-goal'),
  path('delete-goal/<int:goal_id>/', views.delete_goal, name='delete-goal'),
  path('create-goal/', views.create_goal, name='create-goal'),
  path('resources/', views.resources, name='resources'),
  path('add-resource/', views.add_resource, name='add-resource'),
  path('edit-resource/<int:resource_id>/', views.edit_resource, name='edit-resource'),
  path('delete-resource/<int:resource_id>/', views.delete_resource, name='delete-resource'),

  path('book-recommendations/', views.book_recommendations, name='book-recommendations'),
  path('add-book-recommendation/', views.add_book_recommendation, name='add-book-recommendation'),
  path('edit-book-recommendation/<int:book_id>/', views.edit_book_recommendation, name='edit-book-recommendation'),
  path('delete-book-recommendation/<int:book_id>/', views.delete_book, name='delete-book-recommendation'),
  path('guided-exercises/', views.guided_exercises, name='guided-exercises'),
  path('add-meditation-exercise/', views.add_meditation_exercise, name='add-meditation-exercise'),
  path('edit-meditation-exercise/<int:exercise_id>/', views.edit_meditation_exercise, name='edit-meditation-exercise'),
  path('delete-meditation-exercise/<int:exercise_id>/', views. delete_exercise, name='delete-meditation-exercise'),
  path('img2pdf/', views.image, name='img2pdf'),
  path('delete_habit/<int:habit_id>/', views.delete_habit, name='delete_habit'),
  path('timetable-event/', views.timetable_events, name='timetable-event'),
  path('all_events/', views.all_events, name='all_events'), 
  path('add_event/', views.add_event, name='add_event'), 
  path('update/', views.update, name='update'),
  path('remove/', views.remove, name='remove'),
  path('countdown-timer/', views.countdown_timer, name='countdown_timer'),

]
"""
path('timetable/', views.timetable_list, name='timetable-list'),
path('add-timetable-event/', views.add_timetable_event, name='add-timetable-event'),
path('edit-timetable-event/<int:event_id>/', views.edit_timetable_event, name='edit-timetable-event'),
path('delete-timetable-event/<int:event_id>/', views.delete_timetable_event, name='delete-timetable-event'),
path('timetable-events/', views.timetable_events, name='timetable_events'),
"""