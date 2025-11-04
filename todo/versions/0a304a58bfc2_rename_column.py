"""rename column

Revision ID: 0a304a58bfc2
Revises: 9690711caa48
Create Date: 2025-11-04 18:57:34.843403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a304a58bfc2'
down_revision: Union[str, Sequence[str], None] = '9690711caa48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('tasks', 'created_date', new_column_name='Date')


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('tasks', 'Date', new_column_name='created_date')
