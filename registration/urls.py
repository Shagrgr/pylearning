from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('explanation/<str:name>/', views.explanation, name='explanation'),
    path('quize/<str:name>/',views.Quize,name='quize'),
    path('logout/',views.LogoutPage,name='logout'),
    path('profile/',views.ProfilePage,name='profile'),
    path('updatepassword/', views.update_password, name='update_password'),
    path('board/', views.leader_board, name='leader_board'),
    path('game/', views.game, name='game'),
    path('chat/', views.chat, name='chat'),
    path('run_code/', views.run_code, name='run_code'),
    path('gameTopic/<str:topic_name>/', views.gameTopic, name='gameTopic'),
    path('save_note/', views.save_note, name='save_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
   
]
