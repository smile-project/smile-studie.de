from django.db import models


class Email(models.Model):
    email = models.EmailField(unique=True)
    enter_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
