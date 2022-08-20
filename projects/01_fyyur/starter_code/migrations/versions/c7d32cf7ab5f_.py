"""empty message

Revision ID: c7d32cf7ab5f
Revises: e349f516c1aa
Create Date: 2022-08-18 08:21:08.810770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7d32cf7ab5f'
down_revision = 'e349f516c1aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artistgenre', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('venuegenre', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venuegenre', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('artistgenre', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
