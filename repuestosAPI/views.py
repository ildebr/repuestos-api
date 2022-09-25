from django.shortcuts import render
from .models import Repuestos, Venta, Reporte
from .serializers import RepuestosSerializer, VentaSerializer, ReporteSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# Create your views here.

class RepuestosList(generics.ListCreateAPIView):
	#permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    serializer_class = RepuestosSerializer
    def get_queryset(self):
        queryset = Repuestos.objects.all()
        categoria = self.request.query_params.get('categoria')
        if categoria is not None:
            vent = Venta.objects.all()
            print(vent.filter(fecha_venta__range=['2022-08-17', '2022-08-27']))
            print(queryset.filter())
            queryset = queryset.filter(categoria__nombre=categoria)
        return queryset
	

class RepuestosDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes=[IsAuthenticatedOrReadOnly]
	queryset = Repuestos.objects.all()
	serializer_class =RepuestosSerializer

class StandardResultPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 7

class VentaList(generics.ListCreateAPIView):
	#permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = VentaSerializer
    pagination_class = StandardResultPagination
    def paginate_queryset(self, queryset):
        if self.paginator and self.request.query_params.get(self.paginator.page_query_param, None) is None: 
            return None 
        return super().paginate_queryset(queryset)
        # if self.request.query_params.get('page') is None:
        #     return None
        # return StandardResultPagination

    # def get_paginated_response(self, data):
    #     print(self.request.query_params.get('inicio'))
    #     return Response({
    #         'results': data
    #     })

    def get_queryset(self):
        queryset= Venta.objects.all()
        inicio = self.request.query_params.get('inicio')
        final = self.request.query_params.get('final')
        print(inicio)
        if inicio is not None and final is not None:
            print('dentro')
            # queryset = queryset.filter(fecha_venta__range=['2022-08-17', '2022-08-27'])
            queryset = queryset.filter(fecha_venta__range=[inicio, final])
        return queryset
	

class VentaDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes=[IsAuthenticatedOrReadOnly]
	queryset = Venta.objects.all()
	serializer_class =VentaSerializer

class ReporteList(generics.ListCreateAPIView):
	#permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
	

class ReporteDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes=[IsAuthenticatedOrReadOnly]
	queryset = Reporte.objects.all()
	serializer_class =ReporteSerializer
