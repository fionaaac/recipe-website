"""Add preset ingredients

Revision ID: c81473c0397b
Revises: d8ca95ffd9af
Create Date: 2023-11-29 14:47:07.017882

"""
from alembic import op
import sqlalchemy as sa
from recipemain.model import Ingredient

# revision identifiers, used by Alembic.
revision = 'c81473c0397b'
down_revision = 'd8ca95ffd9af'
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


def downgrade():
    pass
