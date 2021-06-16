"""create table state

Revision ID: 751e907a0629
Revises: d5a2251d143e
Create Date: 2021-06-09 21:28:51.790346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '751e907a0629'
down_revision = 'd5a2251d143e'
branch_labels = None
depends_on = None


def upgrade():
    state = op.create_table(
        'state',
        sa.Column('abbrev', sa.String(2), primary_key=True),
        sa.Column('name', sa.String(30), unique=True)
    )
    op.bulk_insert(state,
       [
           {'abbrev': 'AC', 'name': 'Acre'},
           {'abbrev': 'AL', 'name': 'Alagoas'},
           {'abbrev': 'AP', 'name': 'Amapá'},
           {'abbrev': 'AM', 'name': 'Amazonas'},
           {'abbrev': 'BA', 'name': 'Bahia'},
           {'abbrev': 'CE', 'name': 'Ceará'},
           {'abbrev': 'DF', 'name': 'Distrito Federal'},
           {'abbrev': 'ES', 'name': 'Espírito Santo'},
           {'abbrev': 'GO', 'name': 'Goiás'},
           {'abbrev': 'MA', 'name': 'Maranhão'},
           {'abbrev': 'MT', 'name': 'Mato Grosso'},
           {'abbrev': 'MS', 'name': 'Mato Grosso do Sul'},
           {'abbrev': 'MG', 'name': 'Minas Gerais'},
           {'abbrev': 'PA', 'name': 'Pará'},
           {'abbrev': 'PB', 'name': 'Paraíba'},
           {'abbrev': 'PR', 'name': 'Paraná'},
           {'abbrev': 'PE', 'name': 'Pernambuco'},
           {'abbrev': 'PI', 'name': 'Piauí'},
           {'abbrev': 'RJ', 'name': 'Rio de Janeiro'},
           {'abbrev': 'RN', 'name': 'Rio Grande do Norte'},
           {'abbrev': 'RS', 'name': 'Rio Grande do Sul'},
           {'abbrev': 'RO', 'name': 'Rondônia'},
           {'abbrev': 'RR', 'name': 'Roraima'},
           {'abbrev': 'SC', 'name': 'Santa Catarina'},
           {'abbrev': 'SP', 'name': 'São Paulo'},
           {'abbrev': 'SE', 'name': 'Sergipe'},
           {'abbrev': 'TO', 'name': 'Tocantins'}
       ]
   )


def downgrade():
    op.drop_table('state')
