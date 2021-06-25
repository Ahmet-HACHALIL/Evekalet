from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from Evekalet.forms import SignUpForm #, StudentForm   , AgencyForm  , changePasswordForm
from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting , 'page': 'home'}
    return render(request, 'index.html', context)

def contactUs(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting , 'page': 'contactUs'}
    return render(request, 'contactUs.html', context)

def websiteInfo(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting , 'page': 'websiteInfo'}
    return render(request, 'websiteInfo.html', context)

def agency(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting , 'page': 'agency'}
    return render(request, 'agency.html', context)

def loginType(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting , 'page': 'loginType'}
    return render(request, 'loginType.html', context)

def signupType(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting , 'page': 'loginType'}
    return render(request, 'signupType.html', context)

#def box_search(request):
 #   if request.method == 'POST':
  #      form = SearchForm(request.POST)
   #     if form.is_valid():
    #        university_name = Universite.objects.all()
     #       query = form.cleaned_date['query']

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, " Error ! There is a mistake in username or password  ")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # form.password = form.first_name[0:3] + form.email[0:3] ......
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

    form = SignUpForm()
    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)

#def create_student(request):
 #   if request.method == 'POST':
 #       formUser = SignUpForm(request.POST)
 #       formStudent = StudentForm(request.POST)
 #       # form.password = form.first_name[0:3] + form.email[0:3] ......
 #       if formUser.is_valid() & formStudent.is_valid():
 #           formUser.save()
  #          formStudent.save()
  #          username = formStudent.cleaned_data.get('student_id')
  #          password = formStudent.cleaned_data.get('student_id')
  #          user = authenticate(username=username, password=password)
  #          login(request, user)
  #          return HttpResponseRedirect('/')

#    form = StudentForm()
 #   context = {
  #      'form': form,
  #  }

  #  return render(request, 'signup.html', context)
#def changePassword(request):
 #   if request.method == 'POST':
  #      form = changePasswordForm(request.POST)
   #     # form.password = form.first_name[0:3] + form.email[0:3] ......
    #    if form.is_valid():
     #       form.save()
      #      return HttpResponseRedirect('/')

   # form = changePasswordForm()
    #context = {
   #     'form': form,
   # }

 #   return render(request, 'changepassword.html', context)