from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from Adminpanel.models import Student, Institute, User, Program
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from operator import itemgetter
from django.contrib.auth.hashers import make_password
from cryptography.fernet import Fernet
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime, timezone
from pytz import timezone
from datetime import datetime
from Adminpanel.models import AcademicSession
from django.core.paginator import Paginator
import pdb


def decryptedpassword(userPassword):
     key = Fernet.generate_key()
     fernet = Fernet(key)
     decpassword = fernet.decrypt(userPassword).decode()
     return decpassword


def dashboard(request):
     return render(request, 'index-admin.html')


def admin_index(request):
    if request.method == "POST":
     username = request.POST['username']
     password = request.POST['password']
     admin = User.objects.filter(username=username).exists()
     adminDetails = User.objects.filter(username=username)

     if admin == True:
          if adminDetails[0].username == username:
               return render(request, 'index-admin.html')
          else:
               return redirect('/')

    return render(request, "login-admin.html")


def dashboard(request):
     return render(request, "index-admin.html")


def adminlogin(request):
    return render(request, "login-admin.html")


def encryptedpassword(password):
     key = Fernet.generate_key()
     fernet = Fernet(key)
     encpassword = fernet.encrypt(password.encode())
     return encpassword


def createnewuser(request):

     if request.method == "POST":
          user = User()
          user.username = request.POST['username']
          user.password = encryptedpassword(request.POST['password'])
          print(user.password)
          if user.username == "":
               messages.info(request, "some fields are empty")
               return redirect('createnewuser')
          elif User.objects.filter(username=user.username).exists():
               messages.info(request, 'Username already used')
               return redirect('createnewuser')
          else:
               user.save()
               return redirect('/')
     return render(request, 'create-user.html')


def newregistrationverification(request):

     # fetching all objects of tb insistute into a variable
     studiobjall = Institute.objects.all() # fetching all objects of tb insistute into a variable

     studpobjall = Program.objects.all()    # fetching all objects of tb program  into a variable
  
     if request.method == "GET":  # sending get request
          # fetching get request on institute data
          institute_code = request.GET.get('institute_code')
          # fetching get reqiuest on program data
          program_code = request.GET.get('program_code')
          # print(institute_code, program_code)

          # instiute and program is none then context will be pass on
          if institute_code is None and program_code is None:
               context = {
                    'institutes': studiobjall,
                    'program': studpobjall,
                    'InstID': 1,
                    'ProgID': 1,
               }
               return render(request, 'new-registration-verification.html', context)
          else:
               # filter institute objects data
               instID = Institute.objects.filter(code=institute_code).first().id   
               # print(instID) #id
               progID = Program.objects.filter(code=program_code).first().id
               # print(progID) #id
               ans = Student.objects.filter(institute=instID).filter(program=progID)  
                  # filter student table in institute and program
               # print(ans)
               context = {
                         'tasks': ans,
                         'institutes': studiobjall,
                         'program': studpobjall,
                         'InstID': instID,
                         'ProgID': progID,
                    }

               return render(request, 'new-registration-verification.html', context)

     context = {
                    'institutes': studiobjall,
                    'program': studpobjall,
                    'InstID': 1,
                    'ProgID': 1,
               }
     return render(request, 'new-registration-verification.html', context)


def changepassword(request):
     userObject = User.objects.all()
     print(userObject[0].password)
     return render(request, 'change-password.html')


def generateadmitcard(request):

     return render(request, 'generate-admit-card.html')


def registrationcard(request):
     allInfo = Student.objects.all()
     context = {
          'info': allInfo
     }
     return render(request, 'registration-card.html', context)


def pdf_report_create(request, k):  # creating single pdf
     print(k)  # k is our reg_no
     sobj = Student.objects.filter(reg_no=k).first()

     template_path = 'pdf.html'
     context = {
               'details': sobj,
               'newRollNo': k,
     }
     # Create a Django response object, and specify content_type as pdf
     response = HttpResponse(content_type='application/pdf')
     response['Content-Disposition'] = 'attachment; filename='f'{k}.pdf'''
     # find the template and render it.
     template = get_template(template_path)
     html = template.render(context)

     # create a pdf
     pisa_status = pisa.CreatePDF(
          html, dest=response)
     # if error then show some funny view
     if pisa_status.err:
          return HttpResponse('We had some errors <pre>' + html + '</pre>')
     return response


def report(request):
     return render(request, 'repo.html')


def logoutuser(request):
     logout(request)
     return redirect("/")


def pdfdwld(request):
     return redirect('/')


def allpdf(request, i, p):  # Genrating all pdf
     # print(i,p)
     # filter student objects in institue and program table
     ansI = Student.objects.filter(institute=i).filter(program=p)

     # find current time and data of this function
     currenttime = datetime.now(
         timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
     # print( '/', currenttime)

     insI = Institute.objects.filter(id=i).first().name
    # print(insI)

     insP = Program.objects.filter(id=p).first().name
    # print(insP)

     template_path = 'Genratereport.html'

     context = {
               'institute': insI,
               'program': insP,
               'details': ansI,
               'time': currenttime,
     }
     # Create a Django response object, and specify content_type as pdf
     response = HttpResponse(content_type='application/pdf')
     response['Content-Disposition'] = 'attachment; filename='f'{currenttime}.pdf'''
     # find the template and render it.
     template = get_template(template_path)
     html = template.render(context)

     # create a pdf
     pisa_status = pisa.CreatePDF(
          html, dest=response)
     # if error then show some funny view
     if pisa_status.err:
          return HttpResponse('We had some errors <pre>' + html + '</pre>')
     return response

     return redirect(request, "Genratereport.html", {'ans': ans, 't': t})


def update(request, r):
     # fetching all objects of tb insistute into a variable
     studiobjall = Institute.objects.all()
     # fetching all objects of tb insistute into a variable
     studpobjall = Program.objects.all()

     member = Student.objects.get(id=r).id
     print(member)

     members = Student.objects.filter(id=member).update(reg_no=0)
     print(members)
     context = {
                    'institutes': studiobjall,
                    'program': studpobjall,
                    'InstID': 1,
                    'ProgID': 1,
               }
     # member =  Student.objects.POST(reg_no= r)
     # member.update(id = r)
     return redirect(request, 'new-registration-verification.html', context)





def genrateregistrationnumber(request,k):

     if request.method =="GET":

          studiobjall = Institute.objects.all() #fetching all objects of tb insistute into a variable 
          studpobjall = Program.objects.all() 

          context = {

               'institutes': studiobjall,
               'program': studpobjall,
               'instID':1,
               'progID':1,
               'acdemicID':1,
          }
          return render(request, 'new-registration-verification.html', context )

     if request.method == "POST":

          studiobjall = Institute.objects.all() #fetching all objects of tb insistute into a variable 
          studpobjall = Program.objects.all() 
     
          institute_code = request.GET.get('institute_code') 
          program_code = request.GET.get('program_code') 
          academic_session = request.GET.get('academic_session')
          ans = Student.objects.filter(institute = institute_code).filter(program= program_code).filter(academic_session = acdemicID)

          
          instID = Institute.objects.filter(id = institute_code).first()
          print(instID)
          progID = Program.objects.filter(id = program_code).first()
          print(progID)

          acdemicID =  AcademicSession.objects.filter(id = academic_session ).first()
          print(acdemicID)

          # ans = Student.objects.filter(institute = institute_code).filter(program= program_code).filter(academic_session = acdemicID)
          # print(ans)
          
          k = ['instID' + 'progID' + 'acdemicID' + 'ans'].append()

          context = {

               'institutes' : studiobjall,
               'program' : studpobjall,
               'ans' : ans,
               'ans' : k,
               'progID':1,
               'instID':1,
               'acdemicID':1,
               'ans':1,

          }


          return render(request,'new-registration-verification.html', context)






     
     


