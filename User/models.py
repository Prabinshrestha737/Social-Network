from django.db import models

country_choices = [
    ('Nep', 'Nepal'),
    ('Ind', 'India'),
    ('US', 'USA'),
    ('UK', 'United Kingdom'),
    ('Cananda', 'Canada'),
]

gender_choices = [
    ('Male','Male'),
    ('Female', 'Female'),
]

class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    user_name = models.CharField(max_length=50,unique=True)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=10,choices=gender_choices)
    dob = models.CharField(max_length=30)
    country = models.CharField(max_length=30,choices=country_choices)
    profile_pic = models.ImageField()

    def __str__(self):
        self.first_name




    
