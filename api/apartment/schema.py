import graphene
from api.apartment.types import Apartment, ApartmentType


class Query:
    all_apartments = graphene.List(ApartmentType)
    apartments_by_bedrooms = graphene.List(ApartmentType)

    def resolve_all_apartments(self, info):
        return Apartment.objects.all()

    def resolve_apartments_by_bedrooms(self, info, bedrooms):
        return Apartment.objects.filter(bedrooms__exact=bedrooms)


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
