"""Change Apartment special to highlighted

Revision ID: 7572aa030c81
Revises: a10646df083c
Create Date: 2021-07-01 14:55:32.014268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7572aa030c81'
down_revision = 'a10646df083c'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('apartment',
                    'special',
                    nullable=False,
                    server_default=False,
                    existingType=sa.Boolean,
                    type_=sa.Boolean,
                    new_column_name='highlighted')


def downgrade():
    op.alter_column('apartment',
                    'highlighted',
                    nullable=True,
                    existing_server_default=False,
                    existingType=sa.Boolean,
                    type_=sa.Boolean,
                    new_column_name='special')

