from django.contrib import admin
from .models import Persona, Sector, Evento, Asistencia

# Register your models here.

class Admin_Asistencia(admin.ModelAdmin):
    list_display = ["persona", "evento", "timestamp" ]
    list_filter = (
        ("evento"),
    )

    class Meta:
        model = Asistencia


class Admin_Persona(admin.ModelAdmin):
    list_display = ["name", "email", "sector", "phone_number", "birth_date","timestamp"]
    list_filter = (
        ("sector"),

    )
    class Meta:
        model = Persona


admin.site.register(Persona, Admin_Persona)
admin.site.register(Sector)
admin.site.register(Evento)
admin.site.register(Asistencia, Admin_Asistencia)
