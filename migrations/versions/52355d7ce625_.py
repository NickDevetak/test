"""empty message

Revision ID: 52355d7ce625
Revises: cb99ca79479
Create Date: 2014-11-22 14:28:19.157415

"""

# revision identifiers, used by Alembic.
revision = '52355d7ce625'
down_revision = 'cb99ca79479'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('scenario_steps', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'scenario_steps')
    ### end Alembic commands ###
