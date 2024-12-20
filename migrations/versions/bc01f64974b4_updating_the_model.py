"""updating the model

Revision ID: bc01f64974b4
Revises: c13592db425b
Create Date: 2024-11-06 08:16:56.624974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc01f64974b4'
down_revision = 'c13592db425b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('caretaker_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'caretaker', ['caretaker_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('caretaker_id')

    # ### end Alembic commands ###
