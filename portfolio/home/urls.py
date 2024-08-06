from django.contrib import admin
from django.urls import path,include 
from home import views
from . import views

admin.site.site_header="Developer Faizan"
admin.site.site_title="Welcome to Faizan Dashboard"
admin.site.index_title="Welcome to Portal"


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
]
