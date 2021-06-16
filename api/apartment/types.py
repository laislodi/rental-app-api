from graphene_django import DjangoObjectType
from api.apartment.model import Apartment


class ApartmentType(DjangoObjectType):
    class Meta:
        model = Apartment
        fields = ("id", "number", "bedrooms", "description", "price", "available", "special")
