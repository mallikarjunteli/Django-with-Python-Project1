from django.urls import path

from studentapp import views

urlpatterns = [
    path('index',views.index_fun,name='index'),
    path('readdata',views.read_data_fun),
    path('display',views.display_fun,name='display'),
    path('delete/<int:x>',views.delete_fun,name='del'),
    path('update/<int:id>',views.update_fun,name='up'),

    path('register',views.reg_fun,name='register'),
    path('regdata',views.reg_data_fun),
    path('log',views.log_fun,name='log'),
    path('logdata',views.log_read_fun),
    path('home',views.home_fun,name='home'),

    path('logout',views.logout_fun,name='logout')


]