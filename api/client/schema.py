import graphene
from api.client.types import Client, ClientType
from api.service.smtp.mailing import Mailing


class Query:
    all_clients = graphene.List(ClientType)

    def resolve_all_clients(self, info):
        return Client.objects.all()


class SendContactMail(graphene.Mutation):
    class Arguments:
        mail_to = graphene.List(graphene.String)
        subject = graphene.String()
        body = graphene.String()

    ok = graphene.String()

    def mutate(self, info, mail_to, subject, body):
        ok = Mailing().send_contact_email(mail_to=mail_to, subject=subject, body=body)
        return SendContactMail(ok=ok)


class Mutation:
    send_contact_mail = SendContactMail.Field()
