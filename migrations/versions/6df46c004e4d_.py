"""empty message

Revision ID: 6df46c004e4d
Revises: 8a2ed7930152
Create Date: 2020-09-09 17:45:02.859143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6df46c004e4d'
down_revision = '8a2ed7930152'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_commodity', sa.Column('commodityName', sa.String(length=2000), nullable=True, comment='商品名称'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_commodity', 'commodityName')
    # ### end Alembic commands ###