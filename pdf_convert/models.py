from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class pdf(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    pdf_barcode = models.CharField(max_length=25)
    slug = models.SlugField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)