from django.contrib import admin

# Register your models here.
from pdf_convert.models import pdf


class barcodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'pdf_barcode']
    list_filter = ['pdf_barcode']

admin.site.register(pdf, barcodeAdmin)