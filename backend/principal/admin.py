from django.contrib import admin

from .models import Pelicula, Menu, MenuPelicula, ImagenesMuestra


class PeliculaAdmin(admin.ModelAdmin):
    list_display=('titulo','subtitulo')
    list_filter = ('titulo','subtitulo')
    search_fields = ("titulo", )


class MenuAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    list_filter = ('nombre',)
    search_fields = ("nombre", )

class MenuPeliculaAdmin(admin.ModelAdmin):
    model = Menu
    raw_id_fields = ('pelicula','menu')


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuPelicula, MenuPeliculaAdmin)
admin.site.register(ImagenesMuestra)
admin.site.register(Pelicula, PeliculaAdmin)
# admin.site.register(Busqueda)