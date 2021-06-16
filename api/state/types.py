from graphene_django import DjangoObjectType
from api.state.model import State


class StateType(DjangoObjectType):
    class Meta:
        model = State
        fields = ("abbrev", "name")
