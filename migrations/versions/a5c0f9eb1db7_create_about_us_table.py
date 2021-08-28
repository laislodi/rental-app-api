"""Create About_Us table

Revision ID: a5c0f9eb1db7
Revises: 2765bf0da6ed
Create Date: 2021-08-15 19:08:58.366775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5c0f9eb1db7'
down_revision = '2765bf0da6ed'
branch_labels = None
depends_on = None


def upgrade():
    about_us = op.create_table(
        'parameters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('html', sa.TEXT(131070))
    )
    op.bulk_insert(
        about_us,
        [{
            'html': """<div class="container text-center">
<p class="lead">Desde 2006, com a missão de impactar nossos clientes com apartamentos muito bem desenhados, iluminados 
com armários, e com um ótimo preço, oferecemos qualidade de vida mais do que unidades de habitação. </p>
<p>Estamos sempre presentes no prédio para melhor atendê-lo. Contamos com regras de convivência claras e moderadas, 
sempre buscando o bem estar dos nossos clientes e oferecer os melhores serviços. </p>
<p>Procure já os nossos representantes para que possamos oferecer-te o seu próximo apartamento! </p>
<p>Ligue ou envie uma mensagem para ${telephone} ou contate-nos através do email ${email}, ficaremos felizes em 
atendê-lo!</p>
</div>"""
        }]
    )


def downgrade():
    op.drop_table('parameters')
