
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='HOME'),
    path('about',views.about,name='about'),
    path('timetable',views.timetable,name='timetable'),
    path('notification',views.notification,name='notification'),
    path('notes',views.notes,name='notification'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    

]