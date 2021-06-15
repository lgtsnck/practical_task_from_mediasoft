from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Movie


# Create your views here.

class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.all()


class MovieDetailView(DetailView):
    """Детали фильма"""
    model = Movie
    slug_field = "url"


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "moviesapp/register.html"
    success_url = reverse_lazy("movies_view")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("movies_view")


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "moviesapp/login.html"

    def get_success_url(self):
        return reverse_lazy("movies_view")


def logout_user(request):
    logout(request)
    return redirect("movies_view")
