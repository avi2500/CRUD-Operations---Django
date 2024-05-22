from django.urls import path
from todoapp import views


urlpatterns = [
    path('todo/',views.index, name='index'),
    path('todo/add_task/', views.add_task, name='add_task'),
    path('todo/mark_as_done/<int:pk>',views.mark_as_done, name='mark_as_done'),
    path('todo/mark_as_undone/<int:pk>',views.mark_as_undone, name='mark_as_undone'),
    path('todo/edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('todo/delete/<int:pk>',views.delete, name='delete'),
]
