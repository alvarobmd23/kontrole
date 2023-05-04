from django.db import models


class Profile (models.Model):
    profile_name = models.CharField(max_length=100)

    def __str__(self):
        return self.profile_name
