"""empty message

Revision ID: cafe7c2d33c7
Revises: 572c95b37b57
Create Date: 2020-02-20 14:36:21.677693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cafe7c2d33c7'
down_revision = '572c95b37b57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('creator_id', sa.String(length=64), nullable=False))
    op.create_foreign_key(None, 'events', 'staffs', ['creator_id'], ['staff_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'creator_id')
    # ### end Alembic commands ###