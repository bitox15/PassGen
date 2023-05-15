from django.db import models

class Password(models.Model):
    password_text = models.CharField(max_length=255)
    length = models.IntegerField()
    uppercase = models.BooleanField()
    lowercase = models.BooleanField()
    numbers = models.BooleanField()
    special_characters = models.BooleanField()

    def __str__(self):
        return self.password_text