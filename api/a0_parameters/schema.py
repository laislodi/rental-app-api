import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from .model import AboutUs, Parameters


class AboutUsType(DjangoObjectType):
    class Meta:
        model = AboutUs
        fields = ('id', 'html')


class ParametersType(DjangoObjectType):
    class Meta:
        model = Parameters
        fields = (
            'contact_telephone_number', 'facebook_link', 'facebook_text', 'instagram_link', 'instagram_text',
            'contact_email'
        )


class SocialMediaType(ObjectType):
    text = graphene.String()
    link = graphene.String()


class FootParameter(ObjectType):
    telephone = graphene.String()
    email = graphene.String()
    facebook = graphene.Field(SocialMediaType)
    instagram = graphene.Field(SocialMediaType)


class Query:
    get_about_us_html = graphene.String()
    get_foot_parameters = graphene.Field(FootParameter)

    def resolve_get_about_us_html(self, info):
        return AboutUs.objects.first().html

    def resolve_get_foot_parameters(self, info):
        parameters = Parameters.objects.first()
        foot_paramenters = FootParameter(
            telephone=parameters.contact_telephone_number,
            email=parameters.contact_email,
            facebook=SocialMediaType(text=parameters.facebook_text, link=parameters.facebook_link),
            instagram=SocialMediaType(text=parameters.instagram_text, link=parameters.instagram_link)
        )
        return foot_paramenters
