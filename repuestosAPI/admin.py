from django.contrib import admin
from .models import Categoria, Repuestos, Venta, Reporte
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Repuestos)
# admin.site.register(Reporte)
admin.site.register(Venta)


class ReporteAdmin(admin.ModelAdmin):


    def save_related(self, request, form, formsets, change):
        super(ReporteAdmin, self).save_related(request,form, formsets, change)
        vent = Venta.objects.all()
        ventas_delta = vent.filter(fecha_venta__range=[form.instance.fecha_inicio, form.instance.fecha_fin])
        form.instance.ventas.add(*ventas_delta)
admin.site.register(Reporte, ReporteAdmin)


# class ReporteInlinne(admin.TabularInline):
#     model = Reporte

# @admin.register(Venta)
# class VentaAdmin(admin.ModelAdmin):
#     # list_display = ('fecha_inicio', 'fecha_fin')
#     inlines = [ReporteInlinne,]