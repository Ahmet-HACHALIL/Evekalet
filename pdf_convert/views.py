from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render

from Evekalet.settings import EMAIL_HOST_USER
from university.models import Student
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


def show_student_info(request):

    return render(request, 'pdf_convert/showInfo.html')


def pdf_report_create(request):

    post = request.POST
    cs = Student.objects.get(student_id=int(request.POST['studentid']))
    if cs == None:
        messages.error(request, "You have a mistake !!")
        return HttpResponseRedirect('/')

    cs = Student.objects.get(student_name_surname=request.POST['name'])
    if cs == None:
        messages.error(request, "You have a mistake !!")
        return HttpResponseRedirect('/')

    cs2 = User.objects.get(email=request.POST['email'])
    if cs2 == None:
        messages.error(request, "You have a mistake !!")
        return HttpResponseRedirect('/')

    cs3 = request.POST['list']
    if cs3 == 'choose':
        messages.error(request, "You have a mistake !!")
        return HttpResponseRedirect('/')



    student = Student.objects.get(user_id=request.user.id)



    template_path = 'pdf_convert/pdfReport.html'
    context = {'student': student,'cs':cs,'cs2':cs2,'cs3':cs3}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="student_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def send_mail_plain_with_file(request):
    message = 'This file is the agency that your friend created for you'
    mail_id = request.post.get('email','')
    email = EmailMessage(message,EMAIL_HOST_USER,[mail_id])
    email.content_subtype = 'html'

    file = request.FILES['file']
    email.attach(file.name, file.read(), file.content_type)

    email.send()
    return HttpResponse("sent")