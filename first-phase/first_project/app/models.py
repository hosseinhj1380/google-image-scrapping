from django.db import models

# Create your models here.
class scrap_request(models.Model):
    id=models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    title=models.CharField(max_length=50,default=None,blank=False)
    quantity=models.IntegerField(default=10)
    readed=models.BooleanField(default=False,null=False,blank=False)


    def __str__(self):
        return self.title
        
