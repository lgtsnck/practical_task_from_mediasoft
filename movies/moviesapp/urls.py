from django.urls import path

from . import views
from .views import logout_user

urlpatterns = [
    path("movies/", views.MoviesListView.as_view(), name="movies_view"),
    path("movie/<int:pk>/", views.MovieDetailView.as_view()),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    # path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
]
