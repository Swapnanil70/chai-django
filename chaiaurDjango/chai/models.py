from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Eta ekta ORM model - full form is Object Relational Mapping
class ChaiVariety(models.Model):
    # Eta enum jeta mainly database entries er jonno use hoi options
    # restricted korar jonno
    CHAI_TYPE_CHOICES = (
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KESAR'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='chais/', blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='', blank=True, null=True)
    
    # This __str__ method returns the name of the ChaiVariety in the Admin Panel
    # So that the panel looks readable
    def __str__(self):
        """
        Return a string representation of this ChaiVariety.

        This is the name of the ChaiVariety.
        """
        return self.name
    
# One to Many Relationship
# This ForeignKey is for the ChaiVariety model which is used to communicate with the ChaiReview model
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews') # What is this CASCADE? Assignment
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
    
# Many to many relationship
class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores') 
    
    def __str__(self):
        return self.name
    
    
# One to One Relationship
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=200)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.chai.name}'