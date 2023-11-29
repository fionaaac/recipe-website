"""Your migration message

Revision ID: d8ca95ffd9af
Revises: 0476a06e06db
Create Date: 2023-11-29 13:13:54.678145

"""
from alembic import op
import sqlalchemy as sa
from recipemain.model import Ingredient


# revision identifiers, used by Alembic.
revision = 'd8ca95ffd9af'
down_revision = '0476a06e06db'
branch_labels = None
depends_on = None


def upgrade():
    # add preset ingredients 
    op.bulk_insert(Ingredient.__table__, [
        {'name': 'Egg'},
        {'name': 'Milk'},
        {'name': 'Flour'},
        {'name': 'Broccoli'},
        {'name': 'Potato'},
        {'name': 'Tomato'},
        {'name': 'Sugar'},
        {'name': 'Olive Oil'},
        {'name': 'Salt'},
        {'name': 'Pepper'}
    ])
    print("Ingredients added successfully.")


def downgrade():
    pass
