from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=10)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

