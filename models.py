from django.db import models

class Notes(models.Model):
    No = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=10)
    Description = models.TextField()
    Created_on = models.DateTimeField(auto_now_add=True)
    Updated_on = models.DateTimeField(auto_now_add=True)