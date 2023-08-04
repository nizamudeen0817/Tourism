from django.db import models

# Create your models here.
class Tourismcard(models.Model):
    img=models.ImageField(upload_to='pic')
    title=models.CharField(max_length=100,null=True)
    dis=models.CharField(max_length=120)


class Booking(models.Model):
    name=models.CharField(max_length=100)
    phn=models.CharField(max_length=100)
    title=models.ForeignKey(Tourismcard, on_delete=models.CASCADE,null=True)
    Bookingdate=models.DateField(null=True)
    
   