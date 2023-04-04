from django.db import models


class OtpCode(models.Model):
    """model for one time password code"""
    phone = models.CharField(max_length=11, unique=True)
    code  = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.phone} - {self.code} - {self.created}"
    