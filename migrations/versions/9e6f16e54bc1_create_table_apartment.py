"""Create table apartment

Revision ID: 9e6f16e54bc1
Revises: 
Create Date: 2021-06-09 20:27:55.223992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e6f16e54bc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'apartment',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('number', sa.String(4), nullable=False),
        sa.Column('bedrooms', sa.Integer),
        sa.Column('description', sa.String(200)),
        sa.Column('price', sa.Float),
        sa.Column('available', sa.Boolean),
        sa.Column('special', sa.Boolean(200)),
    )


def downgrade():
    op.drop_table('apartment')
