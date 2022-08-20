"""empty message

Revision ID: 44582444acc5
Revises: e1f9514c6655
Create Date: 2022-08-18 09:35:16.836641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44582444acc5'
down_revision = 'e1f9514c6655'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artistgenre', sa.Column('genre_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artistgenre', 'genre_id')
    # ### end Alembic commands ###