from django.db import models
from django.contrib.auth.models import User


class StudySet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class StudySetTerms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_set = models.ForeignKey(StudySet, on_delete=models.CASCADE)
    term = models.CharField(max_length=100)
    definition = models.CharField(max_length=1000)


