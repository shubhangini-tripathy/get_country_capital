from .models import CountryDetail
from rest_framework.serializers import ModelSerializer


class CountryDetailSerializer(ModelSerializer):
    class Meta:
        model = CountryDetail
        fields = ['country', 'capital']
