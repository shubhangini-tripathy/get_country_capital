from .serializers import CountryDetailSerializer
from .models import CountryDetail
from rest_framework import generics

from django.shortcuts import render
from rest_framework import viewsets
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters
#from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import Http404


# Create your views here.
class CountryDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = CountryDetailSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        if pk:
            self.kwargs['pk'] = pk.lower()

        return CountryDetail.objects.filter(country__iexact=pk)
