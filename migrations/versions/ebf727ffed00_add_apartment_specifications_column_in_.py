"""Add apartment specifications column in Apartment table

Revision ID: ebf727ffed00
Revises: 7572aa030c81
Create Date: 2021-07-10 12:07:10.418564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebf727ffed00'
down_revision = '7572aa030c81'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'specifications',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(70), nullable=True),
        sa.Column('apartment_id', sa.Integer, sa.ForeignKey('apartment.id'))
    )


def downgrade():
    op.drop_table('specifications')
