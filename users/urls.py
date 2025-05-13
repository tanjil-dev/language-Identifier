from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict-language/', views.predict_language, name='predict_language'),
    path('api/contact/', views.contact_us, name='contact_us'),
    path('login/', views.custom_login, name='custom_login'),
    path('signup/', views.custom_signup, name='custom_signup'),
    path('logout/', views.custom_logout, name='custom_logout'),
]