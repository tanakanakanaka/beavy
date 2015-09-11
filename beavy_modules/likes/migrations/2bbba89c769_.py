"""empty message

Revision ID: 2bbba89c769
Revises: 33e616d4d32
Create Date: 2015-09-11 12:05:26.783183

"""

# revision identifiers, used by Alembic.
revision = '2bbba89c769'
down_revision = '33e616d4d32'
depends_on = "242c2fd98af"

# add this here in order to use revision with branch_label
branch_labels = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objects', sa.Column('likes_count', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('objects', 'likes_count')
    ### end Alembic commands ###
