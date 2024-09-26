from django.db import models

# Create your models here.
class Reviews(models.Model):
    Gender_Choice = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=Gender_Choice)
    phone_number = models.CharField(max_length=15)
    review = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.name