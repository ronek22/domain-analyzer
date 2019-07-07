"""domain table

Revision ID: 3ea41953cb0e
Revises: 
Create Date: 2019-07-07 21:17:52.097739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ea41953cb0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('domain',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('expiration_date', sa.DateTime(), nullable=True),
    sa.Column('checked', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_domain_name'), 'domain', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_domain_name'), table_name='domain')
    op.drop_table('domain')
    # ### end Alembic commands ###
