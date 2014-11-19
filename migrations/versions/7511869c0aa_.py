"""empty message

Revision ID: 7511869c0aa
Revises: 20556161751
Create Date: 2014-11-18 23:01:38.785529

"""

# revision identifiers, used by Alembic.
revision = '7511869c0aa'
down_revision = '20556161751'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('run_date', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('results', 'run_date')
    ### end Alembic commands ###
