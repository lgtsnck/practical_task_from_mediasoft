from rest_framework import serializers

from .models import Movie


class MovieListSerializers(serializers.ModelSerializer):
    """Список фильмов"""

    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")


class MovieDetailSerializers(serializers.ModelSerializer):
    """Детали фильма"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'


# class RatingSerializer(serializers.ModelSerializer):
#     """Добавление рейтинга пользователем"""
#
#     class Meta:


