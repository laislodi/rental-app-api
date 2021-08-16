"""Create parameter table

Revision ID: 2765bf0da6ed
Revises: ebf727ffed00
Create Date: 2021-07-29 20:29:29.276215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2765bf0da6ed'
down_revision = 'ebf727ffed00'
branch_labels = None
depends_on = None


def upgrade():
    parameters = op.create_table(
        'parameters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('contact_telephone_number', sa.String(25), nullable=False),
        sa.Column('facebook_link', sa.String(200)),
        sa.Column('facebook_text', sa.String(200), default='Facebook'),
        sa.Column('instagram_link', sa.String(200)),
        sa.Column('instagram_text', sa.String(200), default='Instagram'),
        sa.Column('contact_email', sa.String(150), nullable=False),
    )
    op.bulk_insert(parameters, [{
        'contact_telephone_number': '(27) 99820-3636 (Vivo)',
        'facebook_link': 'https://www.facebook.com/lais.lodi.1',
        'facebook_text': 'Arminda Apartamentos',
        'instagram_link': 'https://instagram.com/',
        'instagram_text': 'Arminda Apartamentos',
        'contact_email': 'armindalodi@gmail.com',
        }],
    )


def downgrade():
    op.drop_table('parameters')
