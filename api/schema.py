import graphene
from api.apartment.schema import Query as ApartmentQuery, Mutation as ApartmentMutation
from api.client.schema import Query as ClientQuery
from api.apartmentImages.schema import Query as ApartmentImagesQuery
from api.state.types import StateType


class Query(
    graphene.ObjectType,
    ApartmentQuery,
    ClientQuery,
    ApartmentImagesQuery,
):
    pass


class Mutation(
    graphene.ObjectType,
    ApartmentMutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, types=[StateType, ])
