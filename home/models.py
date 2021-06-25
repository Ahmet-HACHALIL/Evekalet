from django.db import models

# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(blank=True,max_length=255)
    phone = models.CharField(blank=True,max_length=30)
    fax = models.CharField(blank=True,max_length=30)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=30)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=30)
    smtpport = models.CharField(blank=True,max_length=30)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook= models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    website_info = models.TextField()
    contact_us = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title