from rest_framework import serializers

from .models import Movie, Rating, Actor, Genre


class ActorListSerializer(serializers.ModelSerializer):
    """Список Актёров и Режиссёров"""

    class Meta:
        model = Actor
        fields = ("id", "name", "image", )


class ActorDetailSerializer(serializers.ModelSerializer):
    """Актёр или Режиссёр"""

    class Meta:
        model = Actor
        fields = "__all__"


class GenreListSerializer(serializers.ModelSerializer):
    """Список жанров"""

    class Meta:
        model = Genre
        fields = ("id", "name", )


class GenreDetailSerializer(serializers.ModelSerializer):
    """Детали жанра"""

    class Meta:
        model = Genre
        fields = "__all__"


class MovieListSerializers(serializers.ModelSerializer):
    """Список фильмов"""
    rating_user = serializers.BooleanField()
    middle_rating = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ("id", "title", "tagline", "category", "rating_user", "middle_rating")


class MovieDetailSerializers(serializers.ModelSerializer):
    """Детали фильма"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = ActorListSerializer(read_only=True, many=True)
    actors = ActorListSerializer(read_only=True, many=True)
    genres = GenreListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        exclude = ("ip", )

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get("ip", None),
            movie=validated_data.get("movie", None),
            defaults={"value": validated_data.get("value")}
        )
        return rating





