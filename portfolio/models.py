

from django.db import models
from django.contrib.auth.models import User
##code here
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    full_address = models.TextField()
    about_me = models.TextField()
    skills = models.TextField(help_text="Comma-separated skills")

    def __str__(self):
        return self.full_name

class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title