"""empty message

Revision ID: aad55b8e5342
Revises: f3b35b7859ed
Create Date: 2022-08-18 16:11:37.687714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aad55b8e5342'
down_revision = 'f3b35b7859ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('Start_Time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'Start_Time')
    # ### end Alembic commands ###
