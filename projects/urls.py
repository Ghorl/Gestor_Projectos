from django.urls import path
from . import views
urlpatterns = [
    #Enlaces relacionados al login
    path('',views.view_home,name='home'),
    path('register/',views.view_register,name='register'),
    path('logout/',views.view_logout, name='logout'),
    path('login/',views.view_login, name='login'),

    #Enlaces relacionados al project
    path('projects/',views.view_projects,name='projects'),
    path('create_project/',views.view_create_project,name='create_project'),
    path('projects/<int:id>/',views.view_project_detail,name='project_detail'),
    path('projects/<int:id>/create_instrument/',views.view_create_instrument,name='create_instrument'),
    path('instruments/<int:id>/study/',views.view_instrument_detail,name='instrument_detail'),
    path('instruments/<int:id>/study/create_study/', views.view_create_study, name='create_study')

]

