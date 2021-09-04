from django.db import models

# Create your models here.


class ContactForm(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject + ' - ' + self.username + ' <' + self.email + '>'
