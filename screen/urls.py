
from django.urls import path,include
from . import views
urlpatterns = [
  
    path('',views.home,name='home'),
    path('home', views.home, name='home'), 
    path('bio',views.bio,name='bio'),
    path('of-love-war',views.love,name='of-love-war'),
    path('its-what-i-do',views.thirdpage,name='its-what-i-do'),
    path('awards-education',views.awards,name="awards-education"),
    path('Exhibition',views.exhibition,name='Exhibition'),
    path('contact',views.contact,name='contact'),
    path('fine-art-prints',views.art,name='fine-art-prints'),
    path('state/<int:pk>/',views.state,name='state')
    
]