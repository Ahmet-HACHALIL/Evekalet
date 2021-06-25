from django.urls import path
from . import views

urlpatterns = [
    path('MakeAgency', views.show_student_info, name='MakeAgency'),
    path('create-pdf', views.pdf_report_create, name='create-pdf'),
    path('send_mail_plain_with_file', views.send_mail_plain_with_file,name = 'plain_email'),
]