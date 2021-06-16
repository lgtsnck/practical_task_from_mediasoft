from django.contrib import admin
from .models import Category, Actor, Genre, Movie, Shots, Rating
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")
    list_filter = ("category", "date_of_release")
    search_fields = ("title", "category__name")
    save_on_top = True
    save_as = True
    readonly_fields = ("get_image", )
    fieldsets = (
        ("Название и слоган", {
            "fields": (("title", "tagline"), )
        }),
        ("Описание и постер", {
            "fields": (("description", "poster", "get_image"),)
        }),
        ("Дата и страна производства", {
            "fields": (("date_of_release", "country"),)
        }),
        ("Актёры, режиссёры, жанры", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres"),)
        }),
        ("Бюджет и сборы", {
            "fields": (("budget", "usa_fees", "world_fees"),)
        }),
        ("Слаг урлы и категория", {
            "fields": (("url", "category"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="90" height="110"')

    get_image.short_description = "Постер"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="70"')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Rating)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("value", "movie", "ip")


@admin.register(Shots)
class ShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="70"')

    get_image.short_description = "Изображение"


admin.site.site_title = "База фильмов"
admin.site.site_header = "База фильмов"
