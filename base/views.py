from django.shortcuts import render, redirect
from .models import Topic, Message, User, Room, Avatar
from .forms import Register, RoomForm, ProfileUpdate
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.utils import timezone
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    topics = Topic.objects.all()[0:5]
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__first_name__icontains=q)
    )

    p = Paginator(rooms, 10)
    page_number = request.GET.get('page')


    try:
        page_obj = p.get_page(page_number) 
    except PageNotAnInteger:
        page_obj = p.page(1)


    context = {'topics': topics, 'rooms': rooms,  'page_obj':page_obj}
    return render (request, 'base/home.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteRoom(request, pk):
    obj = Room.objects.get(id=pk)
    form = RoomForm(instance=obj)
    if request.method == 'POST':
            obj.delete()
            return redirect ('home')
    context = {'obj': obj}
    return render (request, 'base/delete.html', context)

@login_required(login_url='login')
def deleteMessage(request, pk):
    user= request.user
    obj = Message.objects.get(id=pk)
    author = obj.author
    if request.method == 'POST':
        if user != author:
            return HttpResponse('<h1>ACCESS DENIED</h1>')
        else:
            obj.delete()
            return redirect('home')
    context = {'obj': obj}
    return render(request, 'base/delete.html', context)

@login_required(login_url='login')
def roomChat(request, pk):
    user = request.user
    room = Room.objects.get(id=pk)
    chat_messages = room.message_set.all()
    members =  room.members.all() 
    if request.method == 'POST':
        body = request.POST['text']
        Message.objects.create(
            body = body,
            author = user, 
            room = room
        )
        room.members.add(user)
    context = {'room': room, 'chat_messages' : chat_messages, 'members' : members}
    return render(request, 'base/room.html', context)



@login_required(login_url='login')
def selectAvatar(request, pk):
    avatars = Avatar.objects.all()
    user = User.objects.get(id=pk)
    if request.user == user:
        if request.method == 'POST':
            avatar_id = request.POST.get('avatar')
            if avatar_id:
                # user = request.user
                avatar = Avatar.objects.get(id=avatar_id)
                user.avatar = avatar
                user.save()
                return redirect('home')
    else:
        return HttpResponse('<h1>Access denied</h1>')

    context = {'avatars': avatars}
    return render(request, 'base/avatar.html', context)


@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id = pk)

    context = {'user':user}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def profileUpdate(request, pk):
    user = User.objects.get(id = pk)
    form = ProfileUpdate(instance=user)

    if request.user == user:
        if request.method == 'POST':
            form = ProfileUpdate(request.POST, instance=user)
            # print (form)
            if form.is_valid():
                form.save()
                return redirect('profile', user.id)
    else:
        return HttpResponse('<h1>Access denied</h1>')

    context = {'form': form}
    return render(request, 'base/profile_update.html', context)