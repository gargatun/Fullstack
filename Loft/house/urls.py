from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_complex/', views.about_complex, name='about_complex'),
    path('district/', views.district, name='district'),
    path('apartment_catalog/', views.apartment_catalog, name='apartment_catalog'),
    path('mortgage/', views.mortgage, name='mortgage'),
    path('contacts/', views.contacts, name='contacts'),
    path('sectionmap/', views.sectionmap, name='sectionmap'),
    path('success/', views.success_view, name='success_url'),

    # Добавьте другие маршруты здесь, если нужно
]
