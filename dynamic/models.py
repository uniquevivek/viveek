from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    role = models.CharField(max_length=200, blank=True)

    tech_stack = models.JSONField(default=list, blank=True)

    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    index_number = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['index_number']