from django.db import models
class Rent(models.Model):
    name = models.CharField(
        verbose_name='Rent name',
        max_length=50
    )
    photo = models.ImageField(
        max_length=300,
        upload_to='Rent'
    )
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )
    # phone_no=models.FloatField
    created_at = models.DateTimeField(auto_now_add=True)
    
     
    
    def __str__(self):
        return self.name
