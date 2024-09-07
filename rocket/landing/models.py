from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Hash the password in practice
    account_type = models.CharField(max_length=50, choices=[('founder', 'Founder'), ('joining', 'Joining a team'), ('undecided', 'Undecided')])
    bio_interests = models.TextField()
    bio_background = models.TextField()
    bio_projects = models.TextField()

    def __str__(self):
        return self.email