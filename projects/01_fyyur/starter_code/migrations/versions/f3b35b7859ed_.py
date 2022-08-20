"""empty message

Revision ID: f3b35b7859ed
Revises: b3d4f9cc214a
Create Date: 2022-08-18 12:36:51.118282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3b35b7859ed'
down_revision = 'b3d4f9cc214a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('num_past_shows', sa.Integer(), nullable=True))
    op.drop_column('artist', 'past_shows')
    op.add_column('venue', sa.Column('num_past_shows', sa.Integer(), nullable=True))
    op.drop_column('venue', 'past_shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('past_shows', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('venue', 'num_past_shows')
    op.add_column('artist', sa.Column('past_shows', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('artist', 'num_past_shows')
    # ### end Alembic commands ###