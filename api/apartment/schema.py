import graphene
from django.db.models import Q
from api.apartment.types import Apartment, ApartmentType


class Query:
    all_apartments = graphene.List(ApartmentType)
    apartments_by_bedrooms = graphene.List(ApartmentType)
    apartments_by_bedrooms_at_least = graphene.List(ApartmentType)
    available_apartments = graphene.List(ApartmentType, highlighted=graphene.Boolean())

    def resolve_all_apartments(self, info):
        return Apartment.objects.all()

    def resolve_apartments_by_bedrooms(self, info, bedrooms):
        return Apartment.objects.filter(bedrooms__exact=bedrooms)

    def resolve_apartments_by_bedrooms_at_least(self, info, bedrooms):
        return Apartment.objects.filter(bedrooms__=bedrooms)

    def resolve_available_apartments(self, info, highlighted: bool):
        _filter = Q(available=True)
        if highlighted:
            _filter = _filter & Q(highlighted=True)
        return Apartment.objects.filter(_filter)


class NewApartment(graphene.Mutation):
    class Arguments:
        bedrooms = graphene.Int()
        price = graphene.Float()
        number = graphene.String()
        description = graphene.String()

    apartment = graphene.Field(ApartmentType)

    def mutate(self, info, bedrooms, price, number, description):
        apartment = Apartment(bedrooms=bedrooms, price=price, number=number, description=description)
        apartment.save()
        return NewApartment(apartment=apartment)


class Mutation:
    new_apartment = NewApartment.Field()
