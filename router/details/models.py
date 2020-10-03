from django.db import models

# Create your models here.
class Detail(models.Model):
    sapid = models.CharField(max_length=18)
    hostname = models.CharField(max_length=14)
    loopback = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17)
    is_deleted = models.BooleanField(default=False)

    def deactivate(self):
        obj = self
        obj.is_deleted = True 
        obj.save()      