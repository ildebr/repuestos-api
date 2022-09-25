from django.urls import path
from .views import RepuestosList, RepuestosDetail, VentaList, VentaDetail, ReporteList,ReporteDetail

urlpatterns =[
    path('repuestos/<int:pk>/', RepuestosDetail.as_view(), name='repuestosdetail'),
	path('repuestos/', RepuestosList.as_view(), name="repuestoslist"),
    path('venta/<int:pk>/', VentaDetail.as_view(), name='ventadetail'),
	path('venta/', VentaList.as_view(), name="ventalist"),
    path('reporte/<int:pk>/', ReporteDetail.as_view(), name='reportedetail'),
	path('reporte/', ReporteList.as_view(), name="reportelist"),
]