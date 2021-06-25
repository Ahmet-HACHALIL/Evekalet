from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class University_name(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'image'

class Student(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    university_name = models.ForeignKey(University_name, on_delete=models.CASCADE)
    student_id = models.PositiveIntegerField(primary_key=True)
    student_name_surname = models.CharField(max_length=30)
    college = models.CharField(max_length=255, default='SOME STRING')
    program = models.CharField(max_length=255, default='SOME STRING')
    year = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def image_tag(self):
        return mark_safe('<img src="{}" width="55" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'image'

class Images(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name_surname = models.CharField(max_length=30, default='SOME STRING')
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name_surname

    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'image'