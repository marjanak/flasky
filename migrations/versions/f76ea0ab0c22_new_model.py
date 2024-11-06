"""new model

Revision ID: f76ea0ab0c22
Revises: 31a3f34cd43c
Create Date: 2024-11-05 16:10:43.061652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f76ea0ab0c22'
down_revision = '31a3f34cd43c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('caretaker')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='caretaker_pkey')
    )
    # ### end Alembic commands ###
