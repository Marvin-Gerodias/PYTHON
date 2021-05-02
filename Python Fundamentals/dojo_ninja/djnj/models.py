from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name="ninja", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

