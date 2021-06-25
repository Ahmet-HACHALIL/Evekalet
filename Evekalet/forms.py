from telnetlib import STATUS

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from university.models import Student, University_name


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length = 30, label = 'Student ID ')
    email = forms.EmailField(max_length=200, label='Email ')
    first_name = forms.CharField(max_length=100, label='First Name ')
    last_name = forms.CharField(max_length=100, label='Last Name ')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

#class StudentForm(Student):
 #   university_name = forms.ForeignKey(University_name, on_delete=forms.CASCADE)
  #  student_id = forms.PositiveIntegerField(primary_key=True)
   # student_name_surname = forms.CharField(max_length=30)
  #  college = forms.CharField(max_length=255, default='SOME STRING')
  #  program = forms.CharField(max_length=255, default='SOME STRING')
  #  year = forms.IntegerField()
   # image = forms.ImageField(blank=True, upload_to='images/')
   # status = forms.CharField(max_length=10, choices=STATUS)
   # slug = forms.SlugField()
   # parent = forms.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=forms.CASCADE)
   # create_at = forms.DateTimeField(auto_now_add=True)
   # update_at = forms.DateTimeField(auto_now=True)

    #class Meta:
     #   model = User
      #  fields = ('university_name', 'student_id', 'student_name_surname', 'college', 'program', 'year', 'image', 'status', 'slug', 'parent', 'create_at', 'update_at')

#class AgencyForm(UserCreationForm):
    # mykey = models.CharField(max_length=6, primary_key=True, default=pkgen)
    #client_student_id = forms.IntegerField(max_length=100, label='Agent Student Id ')
    #client_first_name = forms.CharField(max_length=100, label='First Name ')
    #client_last_name = forms.CharField(max_length=100, label='Last Name ')
    #client_university_name = forms.CharField(max_length=100, label='Agent University Name ')

    #agent_student_id = forms.IntegerField(max_length=100, label='Agent Student Id ')
    #agent_first_name = forms.CharField(max_length=100, label='Agent First Name ')
    #agent_last_name = forms.CharField(max_length=100, label='Agent Last Name ')
    #agent_university_name = forms.CharField(max_length=100, label='Agent University Name ')
    #agent_email = forms.EmailField(max_length=200, label='Agent Email ')

    #class Meta:
    #    model = User
    #    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

#class changePasswordForm(UserCreationForm):
 #   password = forms.CharField(max_length = 30, label = 'password ')


  #  class Meta:
   #     model = User
    #    fields = ('password')