from django.conf.urls import url
from django.urls import path
from weightApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('',views.weightdata,name='weightdata'),
    path('',views.getWeight,name='getWeight')
]
