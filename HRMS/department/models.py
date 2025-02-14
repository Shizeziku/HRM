from django.db import models

# Create your models here.

class Department(models.Model):
    Dept_Name=models.CharField(max_length=100,default="dept")
    Description = models.CharField(max_length=300, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.BooleanField(default=True)

    def str(self):
        return (self.Dept_Name)
    
class Roles(models.Model):
    role_name = models.CharField(max_length=100, blank=True,null=True)
    role_description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.BooleanField(default=True)