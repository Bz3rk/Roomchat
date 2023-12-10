from django.shortcuts import render, redirect
from .models import Topic, Message, User, Room
from .forms import Register, RoomForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.







def registration(request):
    form = Register()

    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'base/login_register.html', {'form': form})



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login')


# @login_required(login_url='login')
def home(request):
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    context = {'topics': topics, 'rooms': rooms}
    return render (request, 'base/home.html', context)


def createRoom(request):
    topics = Topic.objects.all()
    host = request.user
    form = RoomForm()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=host,
            topic =topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),)
        return redirect('home')
         
        


    context = {'form': form, 'topics': topics}
    return render(request, 'base/create_room.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics' : topics, 'room': room}
    return render(request, 'base/create_room.html', context)


def deleteRoom(request, pk):
    obj = Room.objects.get(id=pk)
    form = RoomForm(instance=obj)
    if request.method == 'POST':
            obj.delete()
            return redirect ('home')
    context = {'obj': obj}
    return render (request, 'base/delete.html', context)


def roomChat(request, pk):
    user = request.user
    room = Room.objects.get(id=pk)
    chat_messages = room.message_set.all()
    members =  room.members.all() 

    if request.method == 'POST':
        body = request.POST.get('text')
        print(body)
        if body != "":
            message = Message.objects.create(
                room = room,
                author = user,
                body = body
            )
        return redirect('room_chat', pk=room.id)
    

    context = {'room': room, 'chat_messages' : chat_messages, 'members' : members}
    return render(request, 'base/room.html', context)

