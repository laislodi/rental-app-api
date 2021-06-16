import graphene
from api.client.types import Client, ClientType


class Query:
    all_clients = graphene.List(ClientType)

    def resolve_all_clients(self, info):
        return Client.objects.all()
