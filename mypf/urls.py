from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('', views.index, name='home'), #home
    path('portfolio', views.portfolio, name='portfolio'), #portfolio
    path('contact', views.contact, name='contact'), #contact
    path('services', views.services, name='services'), #services
    path('blog', views.blog, name='blog'), #blog
]