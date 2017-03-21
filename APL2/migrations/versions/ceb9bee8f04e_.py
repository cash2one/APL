"""empty message

Revision ID: ceb9bee8f04e
Revises: d152b3e98736
Create Date: 2017-02-09 14:06:10.082881

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ceb9bee8f04e'
down_revision = 'd152b3e98736'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permissions', sa.Column('value', sa.Integer(), nullable=False))
    op.drop_column('permissions', 'val')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permissions', sa.Column('val', mysql.INTEGER(display_width=11), server_default=sa.text("'0'"), autoincrement=False, nullable=False))
    op.drop_column('permissions', 'value')
    # ### end Alembic commands ###