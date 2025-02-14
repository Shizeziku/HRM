from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register, name="register"),
    path('login/',views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('add/', views.add_department, name='add_department'),
    path('update/<int:id>/', views.update_department, name='update_department'),
    path('delete/<int:id>/', views.delete_department, name='delete_department'),
    path('roles/',views.roles,name="roles"),
    path('deleterole/<int:id>/', views.deleterole, name='deleterole'), 
    path('updaterole/<int:id>/',views.updaterole,name='updaterole'),
]