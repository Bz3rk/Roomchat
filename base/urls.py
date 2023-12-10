from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name= 'home'),
    path('registration/', views.registration, name= 'registration'),
    path('login/', views.loginPage, name= 'login'),
    path('logout/', views.logoutUser, name= 'logout'),
    path('create-room/', views.createRoom, name = 'create_room' ),
    path('update-room/<str:pk>', views.updateRoom, name = 'update_room' ),
    path('delete/<str:pk>', views.deleteRoom, name = 'delete' ),
    path('room-chat/<str:pk>', views.roomChat, name = 'room_chat' ),
]