from django.db import models
from catalog.models import Subject, GradeLevel
from users.models import User

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='videos/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='videos')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, related_name='videos')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
