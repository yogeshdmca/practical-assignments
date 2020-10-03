from django.db import models

# Create your models here.

ROUTER_TYPE=(
        ('ag1','AG1'),
        ('css','CSS'),
    )
        
class Router(models.Model):
    loopback = models.CharField("LoopBack", max_length=128, unique=True)
    hostname = models.CharField("Hostname", max_length=128)
    ip = models.GenericIPAddressField()
    type= models.CharField(max_length=20, default='ag1', choices=ROUTER_TYPE)

    def __str__(self):
        return self.hostname