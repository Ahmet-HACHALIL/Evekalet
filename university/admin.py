from django.contrib import admin

# Register your models here.
from university.models import University_name, Student, Images


class University_nameAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'student_name_surname', 'university_name', 'college', 'program','image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'university_name']

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(University_name, University_nameAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Images, ImagesAdmin)
