from django.contrib import admin
from .models import User, TeacherProfile, StudentProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=("username","email","role","is_staff")
    list_filter = ("role",)

# Register your models here.
@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "subjects", "hourly_rate", "is_active")

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "education_level")


