"""changed units to string type

Revision ID: fd7b072f2f81
Revises: 00a583a6a1c7
Create Date: 2023-12-13 21:46:35.059945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd7b072f2f81'
down_revision = '00a583a6a1c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('q__ingredient', schema=None) as batch_op:
        batch_op.alter_column('units',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=64),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('q__ingredient', schema=None) as batch_op:
        batch_op.alter_column('units',
               existing_type=sa.String(length=64),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
