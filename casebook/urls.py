from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('projects/',views.projects, name="projects"),
    path('contact/',views.contact, name="contact"),
    path('resume/', RedirectView.as_view(url='/static/resume/resume.pdf', permanent=False)),
]