from django.db import models
from django.utils import timezone

# TODO: add pictures for project

class Prject(models.Model):
    author = models.ForeignKey('auth.User')
    name_prj = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    finish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.finish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name_prj
