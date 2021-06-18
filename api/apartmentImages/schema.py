import graphene
from api.apartmentImages.types import ApartmentImagesType, ApartmentImage


class Query:
    apartment_images = graphene.List(ApartmentImagesType, apartment_id=graphene.Int())
    apartment_on_focus = graphene.List(ApartmentImagesType)

    def resolve_apartment_images(self, info, apartment_id):
        return ApartmentImage.objects.filter(apartment_id=apartment_id)

    def resolve_apartment_on_focus(self, info):
        return ApartmentImage.objects.filter(apartment__special=True, apartment__available=True)
