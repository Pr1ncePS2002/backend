from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings


class AddCourse(models.Model):
 #   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, null= True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='course_AddCourse', on_delete=models.CASCADE)
    content_id = models.AutoField(primary_key=True)
    U_ID = models.IntegerField(null=True)
    content_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)

    
