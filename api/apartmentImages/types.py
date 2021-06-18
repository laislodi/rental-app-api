from graphene_django import DjangoObjectType
from api.apartmentImages.model import ApartmentImage


class ApartmentImagesType(DjangoObjectType):
    class Meta:
        model = ApartmentImage
        fields = ('id', 'url', 'favorite', 'apartment')
