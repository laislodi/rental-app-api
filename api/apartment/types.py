import graphene
from graphene_django import DjangoObjectType
from api.apartment.model import Apartment
from api.apartmentImages.types import ApartmentImagesType, ApartmentImage


class ApartmentType(DjangoObjectType):
    images = graphene.List(ApartmentImagesType)
    cover_images = graphene.List(ApartmentImagesType)

    def resolve_images(self: Apartment, info):
        return ApartmentImage.objects.filter(apartment=self.id)

    def resolve_cover_images(self: Apartment, info):
        return ApartmentImage.objects.filter(apartment_id=self.id, favorite=True)

    class Meta:
        model = Apartment
        fields = ("id", "number", "bedrooms", "description", "price", "available", "highlighted")
