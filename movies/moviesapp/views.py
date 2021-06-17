from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import models
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Movie, Actor, Genre
from .serializers import MovieListSerializers, MovieDetailSerializers, RatingSerializer, ActorListSerializer, \
    ActorDetailSerializer, GenreListSerializer, GenreDetailSerializer


# Create your views here.

def get_client_api(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class MoviesListView(APIView):
    """Список фильмов"""

    def get(self, request):
        movies = Movie.objects.all().annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_api(request)))
        ).annotate(
            middle_rating=models.Sum(models.F("ratings__value")) / models.Count(models.F("ratings"))
        )
        serializer = MovieListSerializers(movies, many=True)
        return Response(serializer.data)

    # model = Movie
    # queryset = Movie.objects.all()


class AddRatingView(APIView):
    """Добавление рейтинга к фильму"""

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_api(request))
            return Response(status=201)
        else:
            return Response(status=400)


class MovieDetailView(APIView):
    """Детали фильма"""

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serializer = MovieDetailSerializers(movie)
        return Response(serializer.data)

    # model = Movie
    # slug_field = "url"


class ActorListView(generics.ListAPIView):
    """Вывод списка актёров"""
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetailView(generics.RetrieveAPIView):
    """Вывод актёров и режисёров"""
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


class GenreListView(generics.ListAPIView):
    """Вывод списка актёров"""
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer


class GenreDetailView(generics.RetrieveAPIView):
    """Вывод актёров и режисёров"""
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer


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


