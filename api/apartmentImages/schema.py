import graphene
from api.apartmentImages.types import ApartmentImagesType, ApartmentImage


class Query:
    apartment_images = graphene.List(ApartmentImagesType, apartment_id=graphene.Int())

    def resolve_apartment_images(self, info, apartment_id):
        return ApartmentImage.objects.filter(apartment_id=apartment_id)
