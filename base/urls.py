from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name= 'home'),
    path('registration/', views.registration, name= 'registration'),
    path('login/', views.loginPage, name= 'login'),
    path('select-avatar/<str:pk>', views.selectAvatar, name= 'select_avatar'),
    path('profile/<str:pk>', views.profile, name= 'profile'),
    path('profile-update/<str:pk>', views.profileUpdate, name= 'profile_update'),
    path('logout/', views.logoutUser, name= 'logout'),
    path('create-room/', views.createRoom, name = 'create_room' ),
    path('update-room/<str:pk>', views.updateRoom, name = 'update_room' ),
    path('delete-room/<str:pk>', views.deleteRoom, name = 'delete' ),
    path('delete-message/<str:pk>', views.deleteMessage, name = 'delete_message' ),
    path('room-chat/<str:pk>', views.roomChat, name = 'room_chat' ),
    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)