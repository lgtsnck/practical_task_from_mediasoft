from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    """Категории фильмов"""
    name = models.CharField("Категория", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """Актёры и режиссёры"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёр и режиссер"
        verbose_name_plural = "Актёры и режиссеры"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Жанр", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """Фильмы"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default="")
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    date_of_release = models.PositiveIntegerField("Год производства", default=2000)
    country = models.CharField("Страна", max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name="Режиссёр", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актёры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанр")
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать в долларах")
    usa_fees = models.PositiveIntegerField("Сборы в США", default=0, help_text="указывать в долларах")
    world_fees = models.PositiveIntegerField("Сборы в мире", default=0, help_text="указывать в долларах")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Shots(models.Model):
    """Кадры и постеры фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр фильма"
        verbose_name_plural = "Кадры фильма"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=20)
    value = models.SmallIntegerField("Значение", default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return f"{self.value} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
