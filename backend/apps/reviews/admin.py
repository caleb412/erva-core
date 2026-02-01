from django.contrib import admin
from .models import Review, TeacherStats
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("teacher", "rating", "reviewer", "created_at")
    list_filter =  ("rating",)
    search_fields = ("teacher__user__username",)

@admin.register(TeacherStats)
class TeacherStatsAdmin(admin.ModelAdmin):
    list_display = ("teacher", "average_rating", "review_count")