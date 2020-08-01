from django.db import models

# Create your models here.
class Course(models.Model):
	"""docstring for Course"""
	title = models.CharField(max_length=30, blank=True, help_text="Provide course title.", verbose_name="Title")
	description = models.TextField(help_text="Provide course description.", verbose_name="Description")
	course_image = models.FileField(upload_to='course/images', null=True, help_text="upload course vedio.", verbose_name="Course Image")
	
	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name = "Course"
		verbose_name_plural = "Courses"


# Create your models here.
class CourseVideos(models.Model):
	"""docstring for Course"""
	Course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_videos")
	vediofile = models.FileField(upload_to='course/videos', null=True, help_text="upload course vedio.", verbose_name="Vedio File")

	class Meta:
		verbose_name = "Course Video"
		verbose_name_plural = "Course Videos"