"""rename Date column to date

Revision ID: df8931d574d5
Revises: e464dceb54c2
Create Date: 2025-12-18 11:37:21.921782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df8931d574d5'
down_revision: Union[str, Sequence[str], None] = 'e464dceb54c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('tasks', 'Date', new_column_name='date')


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('tasks', 'date', new_column_name='Date')