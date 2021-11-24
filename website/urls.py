from django.urls import path, include
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('et/', views.et, name = 'et'),
    path('es/', views.es, name = 'es'),
    path('rs/', views.rs, name = 'rs'),
    path('courses/', views.courses, name = 'CoursePage'),
    path('courses/<str:name>/', views.courseinfo, name = 'CourseInfo'),
    path('service/', views.services, name = 'ServicePage'),
    path('service/<int:id>/', views.service_detail, name='ServiceDetail'),
    path('team/', views.teams, name = 'team'),
    path('about/', views.about, name = 'about'),
    path('career/', views.career, name = 'career'),
    # path('pay/', views.initiate_payment, name='pay'),
    # path('callback/', views.callback, name='callback'),
    # url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

]
