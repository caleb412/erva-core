from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT","Student"
        TEACHER = "TEACHER", "Teacher"
        ADMIN = "ADMIN","Admin"

    role = models.CharField(
        max_length=20,
        choices= Role.choices,
        default=Role.STUDENT
    )
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class TeacherProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='teacher_profile')
    bio = models.TextField(blank=True)
    subjects = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(default=0)
    hourly_rate = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null = True,
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    def __str__(self):
        return f"Teacher Profile ({self.user.username})"

class StudentProfile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    interests = models.TextField(blank=True)
    learning_goals = models.TextField(blank = True)
    education_level = models.CharField(
        max_length=100,
        blank=True
    )
    preferred_language = models.CharField(
        max_length=50,
        blank = True, 
        help_text="Preferred language for learning"
    )

    def __str__(self):
        return f"Student Profile ({self.user.username})"

