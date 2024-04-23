from django.db import models
#from django.contrib.auth.models import User 


class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField(null=True)
    resource_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
