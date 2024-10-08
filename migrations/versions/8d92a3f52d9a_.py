"""empty message

Revision ID: 8d92a3f52d9a
Revises: e12f79fb1287
Create Date: 2023-10-01 02:18:34.479762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '8d92a3f52d9a'
down_revision: Union[str, None] = 'e12f79fb1287'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('grades', 'name')


def downgrade() -> None:
    op.add_column('grades', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
