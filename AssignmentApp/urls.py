
from django.urls import path
from . import views

app_name = 'AssignmentApp'

urlpatterns = [
    path('', views.index, name='index_temp'),
    path('course-vedios/<int:pk>/', views.allcoursevedios, name="course_vedios_temp"),

]
