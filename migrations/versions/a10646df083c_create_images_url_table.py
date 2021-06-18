"""Create images url table

Revision ID: a10646df083c
Revises: 751e907a0629
Create Date: 2021-06-16 21:05:27.004230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a10646df083c'
down_revision = '751e907a0629'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'apartment_images',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('url', sa.String(200), nullable=False),
        sa.Column('favorite', sa.Boolean),
        sa.Column('apartment_id', sa.Integer)
    )
    op.create_foreign_key(
        'fk_apartment_images_apartment_id', 'apartment_images', 'apartment', ['apartment_id'], ['id']
    )


def downgrade():
    op.drop_constraint('fk_apartment_images_apartment_id', 'apartment_images', type_='foreignkey')
    op.drop_table('apartment_images')
