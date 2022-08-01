from django.shortcuts import render

# Create your views here.
from user.forms import UserRegistrationForm,LoginForm,SongsForm,ArtistsForm
from django.views.generic import CreateView,FormView,TemplateView,ListView
from user.models import User,Songs,Artists
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.contrib import messages
class SignUpView(CreateView):
    model=User
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
class SignInView(FormView):
    model = User
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy("usr-home")
    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if not user:
                return render(request,"login.html",{"form":form})
            print("login success")
            return render(request,"home.html")
class SongCreateView(CreateView):
    model = Songs
    form_class = SongsForm
    template_name = "add-song.html"
    success_url = reverse_lazy("usr-home")

class UserHomeView(TemplateView):
    template_name = "home.html"
class UserSongListView(ListView):
    model = Songs
    context_object_name = "songs"
    template_name = "song-list.html"
class ArtistsCreateView(CreateView):
    model = Artists
    form_class = ArtistsForm
    template_name = "add-artist.html"
    success_url = reverse_lazy("add-song")
class UserArtistsListView(ListView):
    model = Artists
    context_object_name = "artits"
    template_name = "artits-list.html"





