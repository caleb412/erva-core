from django.conf import settings
from django.db import models
from apps.users.models import TeacherProfile
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="given_reviews"
        )
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name="reviews"
         )
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )

    def __str__(self):
            return f"Review({self.rating}) → {self.teacher.user.username}"
    
class TeacherStats(models.Model):
    teacher = models.OneToOneField(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name="stats"
    )
    average_rating= models.FloatField(default=0.0)
    review_count = models.PositiveIntegerField(default = 0)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stats({self.teacher.user.username})"
