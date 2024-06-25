from django.db import models

class Contact (models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    service5 = models.IntegerField(null=True, default=0)
    service1 = models.IntegerField(null=True, default=0)
    service2 = models.IntegerField(null=True, default=0)
    service3 = models.IntegerField(null=True, default=0)
    service4 = models.IntegerField(null=True, default=0)
    message = models.TextField(null=False)
    createDateTime = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.email)