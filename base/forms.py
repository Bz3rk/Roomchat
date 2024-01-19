from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Avatar

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)


        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your valid Email address...'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your First name...'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Last name...'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Password...'})
        self.fields['first_name'].error_messages = {
            'required': 'This field is required.',
            'invalid': 'Enter a valid value.',
        }
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your password...'})
       
        
        

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['host', 'topic', 'name', 'description']
        exclude = ['host']

        
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)



        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Room name...'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Room description...', 'rows': '4', 'cols':'30'})



class ProfileUpdate(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'bio']


    def __init__(self, *args, **kwargs):
        super(ProfileUpdate, self).__init__(*args, **kwargs)


        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Update your First name...'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Update your Last name...'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tell the World a bit about yourself...', 'rows': '4', 'cols':'30'})
