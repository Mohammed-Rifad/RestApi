from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('',views.home,) ,
    path('course/<int:c_id>',views.courseDetail),
    path('course-create',views.addCourse),
    path('course-update/<int:pk>',views.courseUpdate),
    path('course-delete/<int:pk>',views.deleteCourse),
    path('trainer',views.TrainerDetails.as_view()),
    path('trainer/<int:id>',views.TrainerDetails.as_view())
   
]



