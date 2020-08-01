from django.contrib import admin
from .models import Course, CourseVideos
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
    list_display_links = ['title', 'description', 'image']

    def image(self, obj):
        return mark_safe("<img src={0} style='width:35px;height:35px;'>".format(obj.course_image.url))


@admin.register(CourseVideos)
class CourseVideosAdmin(admin.ModelAdmin):
    list_display = ['Course','vediofile']
    list_display_links = ['Course','vediofile']