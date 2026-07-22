from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('MML', "Medium MASALA"),
        ('LML', "Large MASALA"),
        ('GR', "GINGER"),
        ('KL', "KIWI"),
        ('PL', "PLAIN"),
        ('EL', "ELACHI")
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='FirstAPP/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.TextField(default='')

    def __str__(self):
        return self.get_type_display()
    

# One to many Relationship
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# many to many Relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Chai_Varities = models.ManyToManyField(ChaiVarity,related_name='stores')

    def __str__(self):
        return self.name
    
# One to One Relationship

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity,on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'