from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Movie
from .serializers import MovieListSerializers, MovieDetailSerializers


# Create your views here.

class MoviesListView(APIView):
    """Список фильмов"""

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieListSerializers(movies, many=True)
        return Response(serializer.data)

    # model = Movie
    # queryset = Movie.objects.all()


class MovieDetailView(APIView):
    """Детали фильма"""

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serializer = MovieDetailSerializers(movie)
        return Response(serializer.data)

    # model = Movie
    # slug_field = "url"


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
