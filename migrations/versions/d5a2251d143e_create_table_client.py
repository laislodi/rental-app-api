"""Create table client

Revision ID: d5a2251d143e
Revises: 9e6f16e54bc1
Create Date: 2021-06-09 20:41:24.386574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5a2251d143e'
down_revision = '9e6f16e54bc1'
branch_labels = None
depends_on = None

# id           int auto_increment
#         primary key,
#     first_name   varchar(100)  not null,
#     last_name    varchar(100)  not null,
#     rg_number    varchar(12)   null,
#     rg_state     int default 8 null,
#     cpf          varchar(11)   not null,
#     apartment_id int           null,
#     constraint clients_ibfk_1
#         foreign key (apartment_id) references apartments (id),
#     constraint clients_ibfk_2
#         foreign key (rg_state) references states (id)

def upgrade():
    op.create_table(
        'client',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('rg_number', sa.Integer),
        sa.Column('rg_state', sa.String(2)),
        sa.Column('cpf', sa.String(11)),
        sa.Column('apartment_id', sa.Integer),
    )
    op.create_foreign_key(
        'fk_client_apartment_id', 'client', 'apartment', ['apartment_id'], ['id']
    )


def downgrade():
    op.drop_constraint('fk_client_apartment_id', 'client', type_='foreignkey')
    op.drop_table('client')
