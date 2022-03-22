


from django.urls import include, path
from trivia.views import *



urlpatterns = [
    
    path('home/',home,name="home")
]

