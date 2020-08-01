from django.shortcuts import render
from .models import Course, CourseVideos

# Create your views here.
def index(request):
	course_obj = Course.objects.all()
	return render(request, 'index.html', {"course_obj":course_obj})


def allcoursevedios(request, pk):
	course_videos = CourseVideos.objects.filter(Course_id=pk)
	return render(request, 'all_course_vedios.html', {"course_videos_obj":course_videos})
	