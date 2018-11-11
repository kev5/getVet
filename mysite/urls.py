from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite.vetapp import views

urlpatterns = [
	path('', views.home, name='home'),
	path('companies/', views.companies, name='companies'),
	path('signup/', views.signup, name='signup'),
	path('profile/', views.profile, name='profile'),
	path('profile/', views.profile, name='read_more'),
	path('profile/editprofile/', views.editprofile, name='editprofile'),
	path('devprofile/editprofile/', views.editprofile, name='editprofile'),
	path('techprofile/', views.technology, name='technology'),
	path('custprofile/', views.customer, name='customer'),
	path('hr/', views.hr, name='hr'),
	path('admi/', views.admi, name='admi'),
	path('devprofile/', views.dev_profile, name='devprofile'),
	path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
