from django.urls import path
from varzeshkaran.api import views

urlpatterns = [
    path('athletes/', views.get_all_Athletes),
    path('refrees/' , views.get_all_Refrees),
    path('coaches/', views.get_all_coaches),
    path('admins/' , views.admin_list),
    path('athlete/<int:id>' , views.Athlete_Profile),

    
    
    
]