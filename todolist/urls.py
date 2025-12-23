
from django.urls import path , include
from todolist import views

urlpatterns = [
    path('todolist/',views.todolist,name="todolist"),
    path('base/',views.base,name="base"),
    path('home/',views.home,name="home"),
    path('delete_task/<task_id>',views.delete_task,name="delete_task"),
    path('edit_task/<task_id>',views.edit_task,name="edit_task"),
    path('complete_task/<task_id>',views.complete_task,name="complete_task"),
    path('pending_task/<task_id>',views.pending_task,name="pending_task"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('about/', views.about_us, name='AboutUs'),
    path('todolist/',views.todolist,name='tododlist'),
    
   
]
