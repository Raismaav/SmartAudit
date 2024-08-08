from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PruebaSerializer

class PruebaListView(APIView):
    def get(self, request):
        dict_texts = {
            "date": "Fecha de presentación",
            "client": "Cliente",
            "address": "Domicilio",
            "city": "Ciudad",
            "state": "Estado",
            "rfc": "RFC",
            "guide": "Guia",
            "invoice": "Factura",
            "postal_code": "Codigo postal",
            "supplier": "Proveedor",
            "part_number": "Numero de parte",
            "description": "Descripción",
            "quantity": "Cantidad",
            "measure": "medida",
            "fraction": "Fraccion",
            "unit_weight": "Peso unitario",
            "total_weight": "Peso total",
            "gross_weight": "Peso bruto",
            "unit_value": "Valor unitario",
            "total_value": "Valor total",
            "incoterm": "Incoterm"
        }
        serializer = PruebaSerializer(data=dict_texts)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)