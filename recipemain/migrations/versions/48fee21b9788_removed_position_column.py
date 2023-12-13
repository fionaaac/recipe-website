"""removed position column

Revision ID: 48fee21b9788
Revises: dc6a3270ce62
Create Date: 2023-12-13 20:38:22.913013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48fee21b9788'
down_revision = 'dc6a3270ce62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('step', schema=None) as batch_op:
        batch_op.drop_column('position')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('step', schema=None) as batch_op:
        batch_op.add_column(sa.Column('position', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###