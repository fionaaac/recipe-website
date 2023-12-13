"""removed more nullable conditions

Revision ID: 00a583a6a1c7
Revises: f45b35e6ba70
Create Date: 2023-12-13 21:25:51.128400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00a583a6a1c7'
down_revision = 'f45b35e6ba70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('q__ingredient', schema=None) as batch_op:
        batch_op.alter_column('ingredient_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('q__ingredient', schema=None) as batch_op:
        batch_op.alter_column('ingredient_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###