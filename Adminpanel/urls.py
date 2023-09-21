from django.contrib import admin
from django.urls import path,include
from Adminpanel import loginviews

urlpatterns = [

    path('', loginviews.adminlogin, name="login"),
    path('admin_index', loginviews.admin_index, name="admin_index"),
    path('dashboard/', loginviews.dashboard, name="dashboard"),
    path('logoutuser/', loginviews.logoutuser, name="logoutuser"),
    path('admin/createnewuser/', loginviews.createnewuser, name="createnewuser"),
    path('new-registration-verification/', loginviews.newregistrationverification, name="new-registration-verification"),
    path('newregistrationverification', loginviews.newregistrationverification, name="new-registration-verification"),
    path('change-password/', loginviews.changepassword, name="change-password"),
    path('report/', loginviews.report, name="report"),
    path('registration-card/', loginviews.registrationcard, name="registration-card"),
    path('pdf_report_create/<int:k>', loginviews.pdf_report_create, name="pdf_report_create"),
    path('generate-admit-card/', loginviews.generateadmitcard, name="generate-admit-card"),
    path('allpdf/<int:i>/<int:p>/', loginviews.allpdf, name='allpdf'),
    # path('update/<int:r>', loginviews.update, name='update'),
    path('<int:r>/update', loginviews.update, name='update'),
    path('genrateregistrationnumber/<int:k>/', loginviews.genrateregistrationnumber, name='genrateregistrationnumber'),
    path('genrateregistrationnumber', loginviews.genrateregistrationnumber, name='genrateregistrationnumber' )
   
]
