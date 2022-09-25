from rest_framework import serializers
from .models import Repuestos, Venta, Reporte, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class RepuestosSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    class Meta:
        model = Repuestos
        fields = ('categoria', 'nombre', 'descripcion', 'precio_venta', 'unidades_disponible',)

class VentaSerializer(serializers.ModelSerializer):
    repuesto = RepuestosSerializer(     )
    class Meta:
        model = Venta
        fields = ('repuesto', 'cantidad', 'fecha_venta', 'total',)

class ReporteSerializer(serializers.ModelSerializer):
    ventas = VentaSerializer(many=True, required=False)
    class Meta:
        model = Reporte
        fields = ('pk','fecha_inicio', 'fecha_fin','ventas','estado_de_cuenta', 'costo_de_inventario','deficit_de_productos',)
        # optional_fields = ['ventas',]
    
    def create(self, validated_data):
        print(self.context)
        fechai= validated_data.pop('fecha_inicio')
        fechaf= validated_data.pop('fecha_fin')
        reporte = Reporte.objects.create(fecha_inicio=fechai, fecha_fin=fechaf)
        vent = Venta.objects.all()
        ventas_delta = vent.filter(fecha_venta__range=[fechai, fechaf])
        reporte.ventas.add(*ventas_delta)
        acum = 0
        stock = 0
        deficit = 0
        print(ventas_delta)
        for vent in ventas_delta:
            print(vent)
            deficit+=1
            print(vent.total)
            if vent.total:
                acum += vent.total
            if vent.repuesto.costo_compra:
                stock = stock + vent.repuesto.costo_compra * vent.cantidad
        reporte.estado_de_cuenta = acum
        reporte.costo_de_inventario = stock
        reporte.deficit_de_productos = deficit
        reporte.save()
        print(reporte)
        return reporte